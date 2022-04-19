# Fill in this file with the code to get room details from the Webex Teams exercise
import requests
import json

access_token = 'N2VjMGRiNGYtODlhZi00YjM5LWFhOTItNmQwYzI3MzYyMWVhNGFjZGRkY2QtYjNm_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZmU3YThhZjAtOTA1MC0xMWVjLWJhYzMtOGJiY2M0NTJlZGYx'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
