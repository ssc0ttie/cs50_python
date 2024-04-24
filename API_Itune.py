# JSON files - formatted in standard way, but in text files
import json
import requests as req
import sys


if len(sys.argv) != 2:  # name of file and name of band
    sys.exit()

# pretend to be a web brower to access itunes server

response = req.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)

# requests converts the data to a dictionary

print(json.dumps(response.json(), indent=2))

# o = response.json()
# # loops throught the dictionary
# for result in o["results"]:  # the whole of the json file (dic within a dic)
#     # within results dictionary
#     print(result["trackName"])

#     # sys.exit - allows you to exit the program
