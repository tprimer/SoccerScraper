import requests
import json

url = 'http://api.football-data.org/v1/soccerseasons/426/'
APIkey = {'X-Auth-Token':'30bd6dd569b04133ad67fe61d34fb76f'}


print("Making request")
response = requests.get(url,headers=APIkey)
leagueData = json.loads(response.text)
for key,value in leagueData.items():
    if(type(value) is not dict):
        print("{:}: {:}".format(key,value))
    else:
        for k,v in value.items():
            print("    {:}: {:}".format(k,v))

teamsurl = leagueData['_links']['teams']['href']
print("Making request")
response = requests.get(teamsurl,headers=APIkey)
teamData = json.loads(response.text)
print(teamData['teams'][0]['shortName'][0])

for team in teamData['teams']:
    print("{:}".format(team['name']))
