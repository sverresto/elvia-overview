import argparse
import csv
import json


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--date',
                    help='The year and month you want to calculate. ex. 2022-08',
                    required=True)
parser.add_argument('-s', '--surcharge',
                    help='How much the provider adds to the spotpris in øre. Can be negative.',
                    type=float,
                    default= 0)
args = parser.parse_args()

spotprice = '../spot/%s.csv' % args.date
usage     = '../forbruk/%s.json' % args.date
surcharge = args.surcharge

spotmonth = {}

with open('%s' % spotprice) as S:
    spot = csv.reader(S)
    for row in spot:
        if row[0][0] != '2':
            continue
        date, time = row[0].split(' ')
        price = row[-1]
        if not date in spotmonth:
            spotmonth[date] = {}
        spotmonth[date][time] = float(price.replace(',','.'))

def lookupPrice(D):
    # lookup: ['2022-08-02']['06:00:00']
    # input:  2022-08-31T23:00:00+02:00
    date = D[0:10]
    time = D[11:19]
    return spotmonth[date][time]

total = 0.0
cost = 0.0
theirCost = 0.0

with open('%s' % usage) as U:
    J = json.load(U)
    for V in J['meteringpoints'][0]['metervalue']['timeSeries']:
        price = lookupPrice(V['startTime'])
        total += V['value']
        value = V['value']
        cost += price * value
        theirCost += (price+surcharge) * value

print('Total usage kWh: %s' % total)
print('Total cost (spotpris): %s' % cost)
print('Their cost: %s' % theirCost)
