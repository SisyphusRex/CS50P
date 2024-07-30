import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Not enough args")
    try:
        x = float(sys.argv[1])
    except ValueError:
        sys.exit("Not a float")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("bad request")
    o = response.json()
    #print(o["bpi"]["USD"]["rate_float"])
    bitcoin = float(o["bpi"]["USD"]["rate_float"])
    total = x * bitcoin
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()



