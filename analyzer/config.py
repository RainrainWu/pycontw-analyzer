"""
analyzer.config is use to set up static configurations.
"""

from dotenv import load_dotenv


load_dotenv(dotenv_path="../.env")

# raw data directories, using hierarchy structure to concat
# proper directory.
DATA = "./data"

# attendee
ATTENDEE = DATA + "/attendee"
ATTENDEE_STANDARD = ATTENDEE + "/standard.csv"
ATTENDEE_RESERVED = ATTENDEE + "/reserved.csv"
ATTENDEE_DISCOUNT = ATTENDEE + "/discount.csv"

# session
SESSION = DATA + "/session"
