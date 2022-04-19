# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'MjgwMjBkNjAtNzViNi00NTEzLWJmODYtM2U5MjcwNDVlMWRmNGE1ZTEzMjAtZGRj_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'
url = 'https://webexapis.com/v1/teams'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

#Only title parameter is required for this method
params={'name': 'EN2_Devasc_2SNE_EB'}

res = requests.post(url, headers=headers, json=params)
print(res.json())