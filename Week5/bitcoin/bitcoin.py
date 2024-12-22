import requests
import sys
import json

number = sys.argv

# Check if number
try:
    number = float(number[1])
except TypeError:
    sys.exit("Command-line argument is not a number")

# request API
url = url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
try:
    price_list = requests.get(url)
except requests.RequestException:
    sys.exit("Request Exception")

data = price_list.json()
price = data["bpi"]["USD"]["rate_float"]

print(f"${(price * number):,.4f}")