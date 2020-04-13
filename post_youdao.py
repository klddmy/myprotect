import requests
import random
import time

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

content="我和你都是"
class Youdao():
    def __init__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        t=str(random.randint(0,10))
        s=self.ts+t
        print(t)
        print(s)
        return s
            # '15846849464028'

    def get_md5(self,value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()


    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        print("s=",s,"md5=",self.get_md5(s))
        return self.get_md5(s)
            #'c0602e8a7ec7eface095889cad4926f0'


    def get_ts(self):
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        print(ts)
        return ts
             # "1585618581774"

    # def get_content(self):
    #     return content

    def yield_form_data(self):
        form_data={
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '06aea2cce1c727ac4ac3cd80067ea894',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        return form_data


    def get_headers(self):
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=289119002@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=957383472.9889809; JSESSIONID=aaa069b5ycQZu9_U7cYfx; ___rl__test__cookies=1586756358804',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111',
        }
        return headers


    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    # print(form_data)
    # print(get_headers)
    youdao=Youdao('我们')
    print(youdao.fanyi())