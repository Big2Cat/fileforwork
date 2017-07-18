#!/usr/bin/env python
# encoding: utf-8
import sys
import time
import base64
import urllib
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

class LoginWeibo(object):


    def __init__(self):

        self.username = None
        self.password = None
        self.session = requests.Session()

        pass

    def login(self,username,password):

        self.username = username
        self.password = password
        pass
    def get_user_name(self):

        username_quote = urllib.urlencode(self.username)
        username_base64 = base64.b64encode(username_quote)
        return username_base64


    def get_pass_word(self):

        perlogin_params={
            'entry':'weibo',
            'callback':'sinaSSOController.preloginCallBack',
            'su':'',
            'rsakt':'mod',
            'checkpin':'1',
            'client':'ssologin.js(v1.4.18)',
            '_': int(time.time()*1000)
        }
        params_response = self.session.get('https://login.sina.com.cn/sso/prelogin.php',params=perlogin_params)
        pass
