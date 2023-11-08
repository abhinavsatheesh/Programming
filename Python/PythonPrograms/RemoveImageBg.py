# Requires "requests" to be installed (see python-requests.org)
import requests
path = input("Enter file path")
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(path, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'BeoTpZimF517Xc2vFsAN1HLY'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
