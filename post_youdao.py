import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846849464028'


def get_sign():
    return 'c0602e8a7ec7eface095889cad4926f0'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    print(ts)
    return ts
         # "1585618581774"


form_data={
    'i': '我和你都是',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '06aea2cce1c727ac4ac3cd80067ea894',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}

response=requests.post(url,form_data)
print(response.text)