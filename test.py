import json
import requests
import pprint

api_key = 
vimeo_id  = 24096610
vimeo_url = "http://vimeo.com/api/v2/video/%d.json" % vimeo_id

response = requests.get(vimeo_url)

if response.status_code == 200:

    vimeo_data = json.loads(response.content)

    pprint.pprint(vimeo_data)

else:

    print "[*] Failed to retrieve the Vimeo video details. Status Code: %d" % response.status_code
