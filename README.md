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

Spotpris time for time pr måned er lastet ned herfra:
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

