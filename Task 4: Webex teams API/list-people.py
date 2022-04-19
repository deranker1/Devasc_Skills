# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'N2VjMGRiNGYtODlhZi00YjM5LWFhOTItNmQwYzI3MzYyMWVhNGFjZGRkY2QtYjNm_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'

#list details of a registered Webex Teams with email parameter
url = 'https://webexapis.com/v1/people'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

#Only email or id parameter is required for this method
params = {
 'email': 'emin.bilgin@student.pxl.be'
}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))


#Get additional details for a person by using the value of the person id key
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wMTIxZmVkYi1hMjQwLTRjZDgtODg0MS0yZDcwNjYzNzM3MDQ'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

