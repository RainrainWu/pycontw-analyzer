"""
analyzer.config is use to set up static configurations.
"""

from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env")

##############
#  Raw Data  #
##############

# raw data directories, using hierarchy structure to concat
# proper directory.
DATA = "./data"

# attendee
ATTENDEE = DATA + "/attendee"
ATTENDEE_STANDARD = ATTENDEE + "/standard_2019.csv"
ATTENDEE_RESERVED = ATTENDEE + "/reserved_2019.csv"
ATTENDEE_DISCOUNT = ATTENDEE + "/discount_2019.csv"

# program
PROGRAMS = DATA + "/programs"
PROGRAM_2019 = PROGRAMS + "/program_2019.csv"


################
#  Extractors  #
################

# maximum number of row to display while peek data within extractor.
PEEK_MAXIMUM = 5
