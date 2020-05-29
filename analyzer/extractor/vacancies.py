"""
analyzer.extractor.vacancies scrapes job openings from LinkedIn.
"""

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)

from analyzer.extractor import Extractor
from analyzer.config import (
    LINKEDIN_ACCUMULATE_UNREACHABLE_MAXIMUM,
    LINKEDIN_CONSEQUENT_UNREACHABLE_MAXIMUM,
)


class VacancyLinkedIn(Extractor):
    """
    VacancyLinkedIn is a extractor to scrape openings data from LinkedIn.
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    count_xpath = "/html/body/main/div/section/div[2]/h1/span[1]"
    more_xpath = "/html/body/main/div/section/button"
    company_xpath_tpl = "/html/body/main/div/section/ul/li[{id}]/div[1]/h4/a"
    title_xpath_tpl = "/html/body/main/div/section/ul/li[{id}]/div[1]/h3"

    @classmethod
    def extract(cls):
        """
        extract from LinkedIn website.
        """
        page_size = 25
        unreach_accumulate = 0
        unreach_consequent = 0

        cls.driver.get(
            "https://www.linkedin.com/jobs/search/?geoId=104187078&keywords=Python&location=%E5%8F%B0%E7%81%A3"
        )
        item_count = int(cls.driver.find_element_by_xpath(cls.count_xpath).text)
        page_count = int(item_count / page_size) + 1

        for i in range(page_count):

            # collect each vacancy
            cls.driver.implicitly_wait(3)
            for j in range(1, 26):

                index = i * 25 + j
                company_xpath = cls.company_xpath_tpl.format(id=index)
                title_xpath = cls.title_xpath_tpl.format(id=index)
                try:
                    company = cls.driver.find_element_by_xpath(company_xpath).text
                    title = cls.driver.find_element_by_xpath(title_xpath).text
                    cls.hold_data += [[company, title]]
                    unreach_consequent = 0
                except NoSuchElementException:
                    msg_tpl = "Element {id} data unreachable!"
                    print(msg_tpl.format(id=index))
                    unreach_accumulate += 1
                    unreach_consequent += 1

                # abort while excess the unreach times limit
                if (
                    unreach_accumulate > LINKEDIN_ACCUMULATE_UNREACHABLE_MAXIMUM
                    or unreach_consequent > LINKEDIN_CONSEQUENT_UNREACHABLE_MAXIMUM
                ):
                    print(cls.hold_data[-10:])
                    cls.driver.quit()
                    return

            # paging
            try:
                cls.driver.find_element_by_xpath(cls.more_xpath).click()
            except ElementNotInteractableException:
                cls.driver.execute_script(
                    "var q=document.documentElement.scrollTop=300000"
                )

        cls.driver.quit()

    @classmethod
    def transform(cls):
        """
        Copy scraped data.
        """
        cls.export_data = cls.hold_data.copy()


VacancyLinkedIn.extract()
VacancyLinkedIn.transform()
VacancyLinkedIn.peek_export_data()
