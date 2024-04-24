# JSON files - formatted in standard way, but in text files
import json
import requests as req
import sys


try:

    response = req.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    usd_rate = o["bpi"]["USD"]["rate"]

    usd_rate = usd_rate.replace(",", "")
    multi = sys.argv[1]

    rate = float(usd_rate) * float(multi)
    # print("$", round(rate, 4))

    rate_format = "{:,.4f}".format(rate)

    print(f"${rate_format}", sep="")
    # if len(sys.argv) != 2:  # name of file and name of band
    #     sys.exit()

except IndexError:
    print("Missing command-line arguement")
    sys.exit(1)
except ValueError:
    print("Command-line arguement is not a number")
    sys.exit(1)

    # pretend to be a web brower to access itunes server
    # print(sys.argv[1])

    # print(json.dumps(response.json(), indent=2))

    # # loops throught the dictionary
    # for result in o["bpi"]:  # the whole of the json file (dic within a dic)
    #     # within results dictionary
    #     print(result["rate"])

    #     # sys.exit - allows you to exit the program

    # for result in o["bpi"]:
