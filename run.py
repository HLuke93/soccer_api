import requests

url = "https://api-football-v1.p.rapidapi.com/v2/countries"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "64f751dfa5mshee26054ee346f0ap16a79ejsn3b246371d676"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)