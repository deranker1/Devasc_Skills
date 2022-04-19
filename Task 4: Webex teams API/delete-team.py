# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'N2VjMGRiNGYtODlhZi00YjM5LWFhOTItNmQwYzI3MzYyMWVhNGFjZGRkY2QtYjNm_PE93_33d69f74-a9c9-41be-80ba-7fbca5cbedc8'
teamId = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1RFQU0vOTM3ZjRiYjAtYTQ2OC0xMWVjLWEwM2UtNDVjZjc1OTYyZTMy'
url = 'https://webexapis.com/v1/teams/{}'.format(teamId)

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

res = requests.delete(url, headers=headers)
print(res.json())