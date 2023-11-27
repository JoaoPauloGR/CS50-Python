import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        float_arg = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    ...
bitcoin_value = response.json()["bpi"]["USD"]["rate_float"]
bitcoin_answer = bitcoin_value * float_arg
print(f"${bitcoin_answer:,.4f}")