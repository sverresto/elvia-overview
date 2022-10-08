import csv
import json

spotprice = 'spot/2022-08.csv'
usage     = 'forbruk/elvia-2022-08.json'

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

total = 0.0
cost = 0.0
theirCost = 0.0

with open('%s' % usage) as U:
    J = json.load(U)
    for V in J['meteringpoints'][0]['metervalue']['timeSeries']:
        print(V['startTime'])
        print(V['value'])
        price = lookupPrice(V['startTime'])
        total += V['value']
        value = V['value']
        print(value)
        cost += price * value
        theirCost += (price+14.2) * value

print('Total usage kWh: %s' % total)
print('Total cost: %s' % cost)
print('Their cost: %s' % theirCost)
