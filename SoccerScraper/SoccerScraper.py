import requests
import json

url = 'http://api.football-data.org/v1/soccerseasons/426/'
APIkey = {'X-Auth-Token':'30bd6dd569b04133ad67fe61d34fb76f'}


print("Making request")
response = requests.get(url,headers=APIkey)
jData = json.loads(response.text)
print(type(jData))