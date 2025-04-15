import requests
from bs4 import BeautifulSoup

cookies = {
    'OSYM.Antiforgery': 'CfDJ8NJmzo3opmZIhxWcmW0M_YhBXOWmT04Cs5sY8EjCy_7wNazlB_iofNLzhcGzar8NRYF3pnr5HBnB9MehDTe9WQpSDzVjtXH7R3yLnUa8L1LB3FErl248uONEHWYe0z0FPOp4-CeG9TMV4xlZVWHBYx0',
    'OSYM018d6a65': '0148c1759db0ac82201d004446be8a4df470d9d73de6e5fbc5951d148d46d1099e83400bf1a858aefa3dcd159304ed76f2bf6e0aed4ea84e227278e2a5a315effff9df0264',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'OSYM.Antiforgery=CfDJ8NJmzo3opmZIhxWcmW0M_YhBXOWmT04Cs5sY8EjCy_7wNazlB_iofNLzhcGzar8NRYF3pnr5HBnB9MehDTe9WQpSDzVjtXH7R3yLnUa8L1LB3FErl248uONEHWYe0z0FPOp4-CeG9TMV4xlZVWHBYx0; OSYM018d6a65=0148c1759db0ac82201d004446be8a4df470d9d73de6e5fbc5951d148d46d1099e83400bf1a858aefa3dcd159304ed76f2bf6e0aed4ea84e227278e2a5a315effff9df0264',
}

response = requests.get('https://sanalpos.osym.gov.tr/', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
options = soup.find_all("option")

# Her bir option'un value ve görünen metnini yazdır
for option in options:
    print("Value:", option.get("value"))
    print("Text:", option.text)
    print("-" * 40)
