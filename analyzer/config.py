"""
analyzer.config is use to set up static configurations.
"""

from os import path

from dotenv import load_dotenv
from loguru import logger


load_dotenv(dotenv_path="../.env")

##############
#  Raw Data  #
##############

# raw data directories, using hierarchy structure to concat
# proper directory.
DATA = "./data"
if not path.exists(DATA):
    logger.warning("Real data not found, try to analyze with mock data")
    if not path.exists("./mock_data"):
        logger.error("Mock data not found")
        logger.error(
            "please generate data via "
            "`pipenv run python analyzer/utils/mock_data.py`\n"
        )
    else:
        DATA = "./mock_data"

# attendee
ATTENDEE = DATA + "/attendee"
ATTENDEE_STANDARD = ATTENDEE + "/standard_2019.csv"
ATTENDEE_RESERVED = ATTENDEE + "/reserved_2019.csv"
ATTENDEE_DISCOUNT = ATTENDEE + "/discount_2019.csv"
ATTENDEE_COLUMNS = [
    "Years of Using Python / 使用 Python 多久",
    "Area of Interest / 興趣領域",
    "Company  / 服務單位 (For students or teachers, fill in the School + Department Name)",
    'Job Title / 職稱 (If you are a student, fill in "student")',
    "Come From / 國家或地區",
]

# programs
PROGRAMS = DATA + "/programs"
PROGRAMS_2019 = PROGRAMS + "/program_2019.csv"
PROGRAMS_COLUMNS = [
    "title",
    "category",
    "python_level",
    "name",
]

# vacancies
LINKEDIN_ACCUMULATE_UNREACHABLE_MAXIMUM = 10
LINKEDIN_CONSEQUENT_UNREACHABLE_MAXIMUM = 5

###############
#  Mock Data  #
###############

# mock data directories and mocking configuration.
MOCK_DATA = "./mock_data"

# attendee
MOCK_ATTENDEE = MOCK_DATA + "/attendee"
MOCK_ATTENDEE_STANDARD = MOCK_ATTENDEE + "/standard_2019.csv"
MOCK_ATTENDEE_RESERVED = MOCK_ATTENDEE + "/reserved_2019.csv"
MOCK_ATTENDEE_DISCOUNT = MOCK_ATTENDEE + "/discount_2019.csv"
MOCK_ATTENDEE_NUMBER = 200
MOCK_ATTENDEE_AREAS = ["AI/ML", "Data", "Web", "OS", "Algo", "Sec", "Emb"]
MOCK_ATTENDEE_COMPANIES = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
MOCK_ATTENDEE_JOBS = ["R&D", "PM", "CEO", "Co-Founder", "HR", "MK", "BD"]
MOCK_ATTENDEE_COUNTRIES = ["TW", "HK", "JP", "KR", "CH", "AU", "UK", "US"]

# programs
MOCK_PROGRAMS = MOCK_DATA + "/programs"
MOCK_PROGRAMS_2019 = MOCK_PROGRAMS + "/program_2019.csv"
MOCK_PROGRAMS_NUMBER = 40
MOCK_PROGRAMS_CATEGORIES = ["AI/ML", "Data", "Web", "OS", "Algo", "Sec", "Emb"]
MOCK_PROGRAMS_LEVELS = ["NOVICE", "INTERMEDIATE", "EXPERIENCED"]


################
#  Extractors  #
################

# maximum number of row to display while peek data within extractor.
PEEK_MAXIMUM = 5
