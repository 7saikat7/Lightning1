import random
import datetime
dates = []
i = 0
while i < 100:
    year = random.randint(1856, 2020)
    if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        lp = 1
    else:
        lp = 0
    month = random.randint(1, 12)
    if month == 2 and lp == 1:
        day = random.randint(1, 29)
    elif month == 2 and lp == 0:
        day = random.randint(1, 28)
    elif (month <= 7 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    samples = datetime.date(year, month, day)
    b_day = samples.timetuple().tm_yday
    dates.append(b_day)
    i += 1
dates.sort()
i = 0
while i < 100:
    print(dates[i], ":", dates.count(dates[i]))
    i += 1
