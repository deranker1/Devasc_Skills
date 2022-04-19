# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'N2VjMGRiNGYtODlhZi00YjM5LWFhOTItNmQwYzI3MzYyMWVhNGFjZGRkY2QtYjNm_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'
url = 'https://webexapis.com/v1/rooms'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

#Only title parameter is required for this method
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())