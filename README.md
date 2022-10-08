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

Editer `gen-forbruk.py`

```python
year = 2020
month = 2
endyear = 2020
endmonth = 4
```

Generer kommandolinjene som skal kjøres

```bash
~/git/elvia-overview $ python gen-forbruk.py
python get-period.py 2020-02-01T00:00:00 2020-03-01T00:00:00 > forbruk/2020-02.json
python get-period.py 2020-03-01T00:00:00 2020-04-01T00:00:00 > forbruk/2020-03.json
```

## Spotpris

Spotpris for område ØST ligger i `/spot`.

Spotpris time for time pr måned er lastet ned herfra:
<https://minspotpris.no/sjekkfaktura/beregn_fakturagrunnlag.html>

Velg riktig region (viktig!), og måned. 

# eksempler

