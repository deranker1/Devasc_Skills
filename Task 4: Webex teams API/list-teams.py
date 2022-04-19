# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests
import json

access_token = 'N2VjMGRiNGYtODlhZi00YjM5LWFhOTItNmQwYzI3MzYyMWVhNGFjZGRkY2QtYjNm_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'
url = 'https://webexapis.com/v1/teams'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'max': '100'}

res = requests.get(url, headers=headers, params=params)

#Convert the python object "res" into json string with indent of 4
print(json.dumps(res.json(), indent=4))