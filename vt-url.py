import requests

headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"
    }
params = {'apikey': 'b82489dcd39ef37fc9dbe00c8c2b96309c203ac25e51f65b3190af749f466747', 'resource':'http://www.virustotal.com'}

response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=params, headers=headers)

json_response = response.json()

vt_data = json.loads(response.content)

pprint.pprint(vt_data)
