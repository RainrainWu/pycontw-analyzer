"""
analyzer.extractor.vacancies scrapes job openings from LinkedIn.
"""

import csv

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)

from analyzer.extractor import Extractor
from analyzer.config import (
    LINKEDIN_CACHE,
    LINKEDIN_ACCUMULATE_MAXIMUM,
    LINKEDIN_ACCUMULATE_UNREACHABLE_MAXIMUM,
    LINKEDIN_CONSEQUENT_UNREACHABLE_MAXIMUM,
    CAKERESUME_CACHE,
    CAKERESUME_ACCUMULATE_MAXIMUM,
    CAKERESUME_ACCUMULATE_UNREACHABLE_MAXIMUM,
    CAKERESUME_CONSEQUENT_UNREACHABLE_MAXIMUM,
)


class VacancyLinkedIn(Extractor):
    """
    VacancyLinkedIn is a extractor to scrape openings data from LinkedIn.
    """

    hold_data = []
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
        extract from cache if exists, else scrape new.
        """
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        try:
            with open(LINKEDIN_CACHE, newline="") as cache:
                reader = csv.reader(cache)
                cls.hold_data = list(reader)
        except FileNotFoundError:
            logger.warning(LINKEDIN_CACHE + " cache data file not found")
            logger.info(cls.scrape_log_tpl.format(NAME=cls.__name__))
            cls.scrape()

    @classmethod
    def transform(cls):
        """
        Copy scraped data.
        """
        cls.export_data = cls.hold_data

    @classmethod
    def scrape(cls):
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

        cls.hold_data += [["company", "vacancy"]]
        for i in range(page_count):

            # collect each vacancy
            cls.driver.implicitly_wait(5)
            for j in range(1, page_size + 1):

                index = i * page_size + j
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

                # abort while excess the limitations
                if (
                    len(cls.hold_data) >= LINKEDIN_ACCUMULATE_MAXIMUM
                    or unreach_accumulate >= LINKEDIN_ACCUMULATE_UNREACHABLE_MAXIMUM
                    or unreach_consequent >= LINKEDIN_CONSEQUENT_UNREACHABLE_MAXIMUM
                ):
                    cls.driver.quit()
                    cls.write_cache()
                    return

            # paging
            try:
                cls.driver.find_element_by_xpath(cls.more_xpath).click()
            except ElementNotInteractableException:
                cls.driver.execute_script(
                    "var q=document.documentElement.scrollTop=300000"
                )

        cls.driver.quit()
        cls.write_cache()

    @classmethod
    def write_cache(cls):
        """
        Write current holding data into cache file.
        """
        with open(LINKEDIN_CACHE, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            for i in cls.hold_data:
                writer.writerow(i)


class VacancyCakeResume(Extractor):
    """
    VacancyCakeResume is a extractor to scrape openings data from CakeResume.
    """

    hold_data = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    next_xpath_tpl = "/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div[{id}]/div/ul/li[9]/a"
    title_xpath_tpl = "/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div[{id}]/div[1]/div[1]/h2/div/a"
    company_xpath_tpl = "/html/body/div[1]/div/div[2]/div/div/div[1]/div[4]/div/div[{id}]/div[1]/div[1]/h5/a"

    @classmethod
    def extract(cls):
        """
        extract from cache if exists, else scrape new.
        """
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        try:
            with open(CAKERESUME_CACHE, newline="") as cache:
                reader = csv.reader(cache)
                cls.hold_data = list(reader)
        except FileNotFoundError:
            logger.warning(CAKERESUME_CACHE + " cache data file not found")
            logger.info(cls.scrape_log_tpl.format(NAME=cls.__name__))
            cls.scrape()

    @classmethod
    def transform(cls):
        """
        Copy scraped data.
        """
        cls.export_data = cls.hold_data

    @classmethod
    def scrape(cls):
        """
        scrape from StackOverflow website.
        """
        page_size = 10
        page_count = 1
        unreach_accumulate = 0
        unreach_consequent = 0

        url = (
            "https://www.cakeresume.com/jobs?"
            "q=Python&"
            "ref=navs_jobs&"
            "refinementList%5Blocation_list%5D%5B0%5D=%E5%8F%B0%E7%81%A3&"
            "refinementList%5Bprofession%5D%5B0%5D=tech_back-end-development&"
            "refinementList%5Bprofession%5D%5B1%5D=tech_data-engineering&"
            "refinementList%5Bprofession%5D%5B2%5D=tech_data-science&"
            "page=1"
        )
        cls.driver.get(url)

        cls.hold_data += [["company", "vacancy"]]
        while True:
            cls.driver.implicitly_wait(5)

            # collect each vacancies
            for j in range(1, page_size + 1):
                index = (page_count - 1) * page_size + j
                title_xpath = cls.title_xpath_tpl.format(id=index)
                company_xpath = cls.company_xpath_tpl.format(id=index)
                try:
                    cls.hold_data += [
                        [
                            cls.driver.find_element_by_xpath(company_xpath).text,
                            cls.driver.find_element_by_xpath(title_xpath).text,
                        ]
                    ]
                    unreach_consequent = 0
                except NoSuchElementException:
                    msg_tpl = "Element {id} data unreachable!"
                    print(msg_tpl.format(id=index))
                    unreach_accumulate += 1
                    unreach_consequent += 1

                # abort while excess the limitations
                if (
                    len(cls.hold_data) >= CAKERESUME_ACCUMULATE_MAXIMUM
                    or unreach_accumulate >= CAKERESUME_ACCUMULATE_UNREACHABLE_MAXIMUM
                    or unreach_consequent >= CAKERESUME_CONSEQUENT_UNREACHABLE_MAXIMUM
                ):
                    cls.driver.quit()
                    cls.write_cache()
                    return

            # paging
            try:
                cls.driver.execute_script(
                    "var q=document.documentElement.scrollTop="
                    + str(10000 * page_count)
                )
                next_xpath = cls.next_xpath_tpl.format(id=page_size * page_count + 1)
                cls.driver.get(
                    cls.driver.find_element_by_xpath(next_xpath).get_attribute("href")
                )
                page_count += 1
            except NoSuchElementException:
                print("No next page")
                break

        cls.driver.quit()
        cls.write_cache()

    @classmethod
    def write_cache(cls):
        """
        Write current holding data into cache file.
        """
        with open(CAKERESUME_CACHE, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            for i in cls.hold_data:
                writer.writerow(i)


VacancyLinkedIn.extract()
VacancyLinkedIn.transform()
VacancyCakeResume.extract()
VacancyCakeResume.transform()
