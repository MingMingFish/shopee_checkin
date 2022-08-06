import requests
url = 'https://shopee.tw/mkt/coins/api/v2/checkin_new'
headers = {
    "authority": "shopee.tw",
    "method": "POST",
    "path": "/mkt/coins/api/v2/checkin_new",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "content-length": "0",
    "cookie": '''_fbp=fb.1.1621402512407.723496175; csrftoken=OENmL43jizG6JzWpdThInXj5ypXwIE7V; SPC_F=r2wSEkgHBuQ6ZWsObhcVB6EsEFVDNMAR; REC_T_ID=fc6b5ce6-b863-11eb-b579-b496914619c0; __BWfp=c1621402514824x4bf11a23a; G_ENABLED_IDPS=google; SPC_CLIENTID=cjJ3U0VrZ0hCdVE2pjaikyagvqmpeezh; welcomePkgShown=true; SPC_PC_HYBRID_ID=41; _fbc=fb.1.1624847193718.IwAR1IEbIdfcNDddThKud86_ec0IuA754lV1ar1X3mHVI1otKvaD8ej0Z4BYY; _ga_8XD7H14FP3=GS1.1.1628369801.2.0.1628369801.0; REC_T_ID=229b79f4-17e8-11ec-8382-d0946659c941; _QPWSDCXHZQA=fe40ec75-5ab9-47bf-9e09-aa25f1b7865d; _bwgaid=1647919258.1621402513; spc_ckt_reqid=1f8a1b84d5c1318cd6a88bbcfc5d1a00:0100016e2dc235f3:000000218b93f197; __LOCALE__null=TW; __stripe_mid=80318344-b360-4484-aec5-936393c41d7d22512a; SPC_LIUP_126032488=; _gcl_au=1.1.164862897.1656028394; kk_leadtag=true; SPC_ST=.RE91Z0pza3lZelBJWmVlRP5kX8lTv57syi2E5GVzymbW7DhP4N901GjryBJEfw9pe6jdu+wK+99EP8aoswCU9Xybc1JvLFj8813dk6GJzwAT5zyKd01AHFeORAxG+4UQ3MkPPJy4DCFMn1JpETQUZqZS76nOHI0xVi3HzGWgwQyK2xGRAqg9v9Z+oGBjbt7WlIMc+DzWa9t6d170dfRPBg==; _ga_KK6LLGGZNQ=GS1.1.1659160894.8.0.1659160898.0; SPC_U=126032488; SPC_T_ID="2wc8vj08kpLgDMHxNkatAF9PmROGT7RNrIAniVZoaOo7mY5XNdGHNcMomkRiZiE515o2ZLUJ4KvwblMT6NW2xK7wXwcHF/9CNXaRNtURcz8="; SPC_T_IV="pZ1c2fz5c6PhJuOco7/gxw=="; SPC_T_ID=2wc8vj08kpLgDMHxNkatAF9PmROGT7RNrIAniVZoaOo7mY5XNdGHNcMomkRiZiE515o2ZLUJ4KvwblMT6NW2xK7wXwcHF/9CNXaRNtURcz8=; SPC_T_IV=pZ1c2fz5c6PhJuOco7/gxw==; SPC_SI=mall.upXfDAzFcjnPSUFlKVRUHS63dOSn8ksv; _gid=GA1.2.1998222465.1659605778; SPC_IA=1; SPC_R_T_ID=2wc8vj08kpLgDMHxNkatAF9PmROGT7RNrIAniVZoaOo7mY5XNdGHNcMomkRiZiE515o2ZLUJ4KvwblMT6NW2xK7wXwcHF/9CNXaRNtURcz8=; SPC_R_T_IV=pZ1c2fz5c6PhJuOco7/gxw==; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1647919258.1621402513; cto_bundle=AjBSpV9JemN3YW5GRlRaemwyb05PNktmVjZHTVRMVk1pNU5sSFlxUHFPbmZUeXo1STh4eXVKZUJFdzlXWlFwREt0R2NxQ2Y4RTBZYUxCNjdKJTJGbTBYSTFwbjFNdGJzVHVONmtoVXUwWDZ3YkNtZTNwemFxUkdTWTNVMzM1VjRwMlJuTUcwc3Q0ZHg2RFJlU1FQWTFzdjRFTmswUSUzRCUzRA; shopee_webUnique_ccd=xNfn9K%2B0ltf72OESA3Xhxw%3D%3D%7C%2BvNFmO98cJ5rYh4batdgsS713coR7M2XDF9kHNTj9lOGFPjI6wJ5fiRfD5Sqso5UTHYyPPh6uJN0Ne5jwjC7j9CRXGg%3D%7C92rPQo0dbYaJ9sOO%7C05%7C3; _ga_RPSBE3TQZZ=GS1.1.1659632064.214.1.1659632075.49; SPC_EC=QjVCU3Q3RTVDdnhYajVuUKYnHNsBv/4smJv+8kdvRnqUSJg/G/KldwHoqBg3vO7L55QAYHOcIjsJ37D0QI2iz3RJiYFeYuxjvrtbUozEB07AZMcW+JhKZ2ifWG5tmhxRTLKTfwqi7v7nY49kwbngV92l2SKGp+THhbwibhGYiG4=''',
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