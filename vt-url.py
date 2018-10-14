import requests

headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"
    }
params = {'apikey': 'insert api key here', 'resource':'http://www.virustotal.com'}

response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=params, headers=headers)

json_response = response.json()

vt_data = json.loads(response.content)

pprint.pprint(vt_data)
