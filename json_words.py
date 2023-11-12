import requests
import json


request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/wonderful")
data = request.json()[0]
