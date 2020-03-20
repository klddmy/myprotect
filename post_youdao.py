import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

form_data={
    'i': '我和你都是',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846849464028',
    'sign': 'c0602e8a7ec7eface095889cad4926f0',
    'ts': '1584684946402',
    'bv': '06aea2cce1c727ac4ac3cd80067ea894',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}

response=requests.post(url,form_data)
print(response.text)