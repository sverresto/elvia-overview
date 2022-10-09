import argparse
import calendar

from datetime import datetime


parser = argparse.ArgumentParser(description="Helper to generate command line needed to fetch data from Elvia")

parser.add_argument('-s', '--start',
                    help='The year and month you want to calculate from. ex. 2022-05',
                    required=True)
parser.add_argument('-e', '--end',
                    help='The year and month you want to calculate to. ex. 2022-08',
                    required=True)

args = parser.parse_args()

# set this to the period you like to fetch data from
year,month = map(int, args.start.split('-'))
endyear,endmonth = map(int, args.end.split('-'))

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
