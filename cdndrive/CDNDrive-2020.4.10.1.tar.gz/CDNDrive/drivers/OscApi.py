# coding: utf-8

import sys
import base64
import hashlib
import random
import requests
import rsa
import time
import re
from urllib import parse
from CDNDrive.util import *

class OscApi:

    default_hdrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    default_url = lambda self, hash: f"https://oscimg.oschina.net/oscnet/up-{hash}.png"
    extract_hash = lambda self, s: re.findall(r"\w{35}", s)[0]    

    def __init__(self):
        self.cookies = load_cookies('osc')
        
    def meta2real(self, url):
        if re.match(r"^osdrive://\w{35}$", url):
            return self.default_url(self.extract_hash(url))
        else:
            return None
            
    def real2meta(self, url):
        return 'osdrive://' + self.extract_hash(url)
        
    def login(self, un, pw):
        return {
            'code': 114514,
            'message': '功能尚未实现，请使用 Cookie 登录'
        }
        
    def set_cookies(self, cookie_str):
        self.cookies = parse_cookies(cookie_str)
        save_cookies('osc', self.cookies)
        
    def get_user_info(self, fmt=True):
        return '获取用户信息功能尚未实现'
        
    def image_upload(self, img):
            
        url = 'https://my.oschina.net/wizardforcel/space/markdown_img_upload'
        files = {'editormd-image-file': (f"{time.time()}.png", img, 'image/png')}
        try:
            r = request_retry(
                'POST', url, 
                files=files, 
                headers=OscApi.default_hdrs,
                cookies=self.cookies
            )
        except Exception as ex:
            return {'code': 114514, 'message': str(ex)}
        
        if r.status_code != 200:
            return {
                'code': r.status_code,
                'message': f'HTTP {r.status_code}'
            }
        j = r.json()
        
        j['code'] = 1 - j['success']
        if j['code'] == 0:
            j['data'] = j['url']
        return j
        
def main():
    op = sys.argv[1]
    if op not in ['cookies', 'upload']:
        return
        
    api = OscApi()
    if op == 'cookies':
        cookies = sys.argv[2]
        api.set_cookies(cookies)
        print('已设置')
    else:
        fname = sys.argv[2]
        img = open(fname, 'rb').read()
        r = api.image_upload(img)
        if r['code'] == 0:
            print(r['data'])
        else:
            print('上传失败：' + r['message'])
    
if __name__ == '__main__': main()