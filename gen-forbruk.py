from datetime import *
import calendar

# set this to the period you like to fetch data from
year = 2020
month = 2
endyear = 2020
endmonth = 4

# Not much to du below this comment
oldyear = 0
oldmonth = 0

while 1:    
    start = datetime.strptime('%s-%s-%s' % (int(year), int(month), '01'), '%Y-%m-%d')
    oldyear = year
    oldmonth = month
    
    if month == 12:
        year = year + 1
        month = 1
    else:
        month += 1

    end = datetime.strptime('%s-%s-%s' % (int(year), int(month), '01'), '%Y-%m-%d')
    print("python get-period.py %s %s > forbruk/%s-%02d.json" % (start.isoformat(), end.isoformat(), oldyear, oldmonth))
    
    if year == endyear and month == endmonth:
        break
