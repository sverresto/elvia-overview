# elvia-overview

Download your electric usage data, and generate interesting stats.

## installer elvia-python

<https://github.com/andersem/elvia-python>

```bash
pip install --upgrade elvia
```

## Autentiser

```bash
# 1100 random letters and numbers
export ELVIA_METER_VALUE_TOKEN=""

# 18 digits
export ELVIA_METERING_POINT_ID=""
```

## bruk

```bash
$ python gen-forbruk.py -s 2022-05 -e 2022-08
python get-period.py 2022-05-01T00:00:00 2022-06-01T00:00:00 > forbruk/2022-05.json
python get-period.py 2022-06-01T00:00:00 2022-07-01T00:00:00 > forbruk/2022-06.json
python get-period.py 2022-07-01T00:00:00 2022-08-01T00:00:00 > forbruk/2022-07.json
```

## Spotpris

Spotpris for område ØST ligger i `/spot`.

Spotpris time for time pr måned er lastet ned herfra, og lagret som csv (etter å ha fjernet de to kolonnene til høyre):
<https://minspotpris.no/sjekkfaktura/beregn_fakturagrunnlag.html>

Velg riktig region (viktig!), og måned. 

## eksempler

### `bill.py`

Regner sammen timesforbruk og spotpris for en måned. `-s` vil legge til ørepåslag, `-c` vil legge til faste gebyrer.

```bash
$ python bill.py -d 2022-06
Total usage kWh: 1020.8450000000001
Total cost (spotpris): 192060.43737400026
Their cost: 192060.43737400026
```

### stats.py

Regner ut det daglige timesforbruket, og summerer dagene.

```bash
$ python stats.py -d 2022-06
'00:00:00','73.94037897899999','41.572'
'01:00:00','61.455086322999996','35.253'
'02:00:00','54.975956276','31.814000000000007'
'03:00:00','50.781662095','29.978999999999992'
'04:00:00','49.066167558999986','29.229'
'05:00:00','49.610034730999985','29.329'
'06:00:00','56.027158576999994','30.156999999999993'
'07:00:00','108.612389048','52.611'
'08:00:00','93.980469865','44.022999999999996'
'09:00:00','94.31682581400001','43.52399999999999'
[...]
```

I juni brukte vi mest strøm mellom 07 og 08...
