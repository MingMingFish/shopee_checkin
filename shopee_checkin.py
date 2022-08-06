import requests
url = 'https://shopee.tw/mkt/coins/api/v2/checkin_new'
with open('cookie.txt','r') as f:
    cookie = f.read()

headers = {
    "authority": "shopee.tw",
    "method": "POST",
    "path": "/mkt/coins/api/v2/checkin_new",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "content-length": "0",
    "cookie": cookie,
    "origin": 'https://shopee.tw',
    "referer": "https://shopee.tw/shopee-coins",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

website = requests.post(url,headers=headers)
print('Completed')