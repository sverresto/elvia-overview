import argparse
import csv
import json


parser = argparse.ArgumentParser(description="Sum every hour in a month, to see which our is using most power")

parser.add_argument('-d', '--date',
                    help='The year and month you want to calculate. ex. 2022-08',
                    required=True)
args = parser.parse_args()

spotprice = '../spot/%s.csv' % args.date
usage     = '../forbruk/%s.json' % args.date

spotmonth = {}

with open('%s' % spotprice) as S:
    spot = csv.reader(S)
    for row in spot:
        if row[0][0] != '2':
            continue
        date, time = row[0].split(' ')
        price = row[-1]
        # print('%s, %s, %s' % (date, time, price))
        if not date in spotmonth:
            spotmonth[date] = {}
        spotmonth[date][time] = float(price.replace(',','.'))

def lookupPrice(D):
    # lookup: ['2022-08-02']['06:00:00']
    # input:  2022-08-31T23:00:00+02:00
    date = D[0:10]
    time = D[11:19]
    return spotmonth[date][time]

byHour = {}

with open('%s' % usage) as U:
    J = json.load(U)
    for V in J['meteringpoints'][0]['metervalue']['timeSeries']:
        #print(V['startTime'])
        #print(V['value'])
        price = lookupPrice(V['startTime'])
        time = V['startTime'][11:19]
        if not time in byHour:
            byHour[time] = { 'usage': 0, 'cost': 0 }
        byHour[time]['usage'] += V['value']
        byHour[time]['cost'] += (V['value']*price)/100
        
#print(byHour)
for H in byHour:
    print("'%s','%s','%s'" % (H, byHour[H]['cost'], byHour[H]['usage']) )
