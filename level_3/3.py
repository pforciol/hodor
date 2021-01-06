#!/usr/bin/python3.6
import requests
import os
from bs4 import BeautifulSoup

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from PIL.Image import core as _imaging

URL = 'http://158.69.76.135/level3.php'
ID = '2500'

check = ID + "    </td>\n    <td>\n1024"

r = requests.get(URL, allow_redirects=False)
soup = BeautifulSoup(r.text, 'html.parser')

key = soup.find('input', {'name': 'key'}).get('value')
cookies = r.cookies
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Referer': URL
}

payload = {'id': ID, 'holdthedoor': 'submit', 'key': key, 'captcha': ''}


def captcha():
    image_r = requests.get('http://158.69.76.135/captcha.php',
                           cookies=cookies, headers=headers)

    with open('./image.php', 'wb') as f:
        f.write(image_r.content)

    captcha = pytesseract.image_to_string(Image.open('./image.php')).strip()
    os.remove('./image.php')
    return captcha


while check not in r.text:
    payload['captcha'] = captcha()
    r = requests.post(URL, data=payload, headers=headers, cookies=cookies)

print("Done")
