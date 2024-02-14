from db import *

class backend:

    def __init__(self, database):
        self.database = Database(database)

    # Input: Using the calendar library, our dates are given in "mm/dd/yy", or "m/d/yy"
    # Output: A comparable date number "yymmdd"
    def parseDate(self, dateString):
        dateList = dateString.split('/')
        return f"{dateList[2].rjust(2, '0')}{dateList[0].rjust(2, '0')}{dateList[1].rjust(2, '0')}"
    