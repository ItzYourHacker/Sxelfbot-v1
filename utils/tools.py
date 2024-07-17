from pycoingecko import CoinGeckoAPI
import requests
from utils.config import *


cg = CoinGeckoAPI()

def ltc_to_usd():
    try:              
      response = cg.get_price(ids='litecoin', vs_currencies='usd')
      return response['litecoin']['usd']
    except Exception as e:
        print(e)


def usd_to_satoshis(usd_amount):
  try:
    ltc_to_usd_price = ltc_to_usd()
    ltc_price_in_satoshi = 100_000_000
    satoshis_amount = int(usd_amount / ltc_to_usd_price *
                          ltc_price_in_satoshi)
    return satoshis_amount
  except Exception as e:
      print(e)

def satoshis_to_ltc(satoshis_amount):
  try:
    ltc_price_in_satoshis = 100_000_000
    ltc_amount = satoshis_amount / ltc_price_in_satoshis
    return ltc_amount
  except Exception as e:
      print(e)


def send_litecoin(addy, amount):
  try:
    url = "https://api.tatum.io/v3/litecoin/transaction"
    payload = {
        "fromAddress": [{
            "address": ltc_addy,
            "privateKey": pvt_key
        }],
        "to": [{
            "address": addy,
            "value": amount
        }],
        "fee": "0.0005",
        "changeAddress": ltc_addy
    }
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(data)
    return data
  except Exception as e:
    print(e)


