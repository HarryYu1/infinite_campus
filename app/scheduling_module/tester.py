import find_lowest
from datetime import datetime

currentDate = datetime.now()

date_str = '09-01-2022'
soarDate = datetime.strptime(date_str, '%m-%d-%Y')

find_lowest.write_to_database(currdate=currentDate, soardate=soarDate)