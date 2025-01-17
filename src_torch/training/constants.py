

from re import M

from pytz import HOUR


HISTORY_LEN = 150
MIN_CONTEXT = HISTORY_LEN - 10
PADDING = HISTORY_LEN - MIN_CONTEXT
TARGET_LEN = 24
TRIM_LEN = TARGET_LEN + max(0, MIN_CONTEXT - 2 * TARGET_LEN)
TARGET_INDEX = TARGET_LEN + TRIM_LEN

YEAR = 0
MONTH = 1
DAY = 2
DOW = 3
DOY = 4
HOUR = 5
MINUTE = 6

# Tasks
SINGLE_POINT = 0
MEAN_TO_DATE = 1
STDEV_TO_DATE = 3
NUM_TASKS = 10