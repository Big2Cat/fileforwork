#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib,urllib2
import hashlib
from urllib import urlencode

def main():
    #配置您申请的APPKey
    appkey = "geetest"
    #调用requestTarget1函数
    requestTarege1("GET")

#Step1: GET目标网站
def requestTarege1(m="GET"):
    #验证码的url地址
    url="https://bpassport.ch.com/LimitTest/Captcha"

    if m =="GET":
        f = urllib.urlopen("%s" % (url))
    else:
        f = urllib.urlopen(url)

    content = f.read()
    res = json.loads(content)
    #获取gt
    targetGt = res['gt']
    #获取challenge
    targetChallenge = res['challenge']

    requestClever("geetest",targetGt,targetChallenge,"GET")

#Step2: 调用聪明力
def requestClever(appkey,_targetGt,_targetChallenge,m="GET"):
    url = "http://dev.cleverli.cn:8310/api/captcha/geetest"
    params_url = "appid=geetest&challenge=%s&gt=%s&referer=https://www.ch.com/&signinfo=" % (_targetChallenge,_targetGt)
    params_sign = "appid=geetest&challenge=%s&gt=%s&referer=https://www.ch.com/&geetest" % (_targetChallenge,_targetGt)

    #封装签名
    md = hashlib.md5()
    md.update(params_sign)
    sign=md.hexdigest()

    if m =="GET":
        testurl = "%s?%s%s" % (url,params_url,sign)
        f=urllib.urlopen(testurl)
    else:
        f = urllib.urlopen(url, params_url)

    content = f.read()
    res = json.loads(content)

    c_validate = res["validate"]
    c_challenge = res["challenge"]

    requestTarget2(c_validate,c_challenge,m="POST")

#STEP3: POST目标网页
def requestTarget2(_validate,_challenge,m="POST"):
    url="https://bpassport.ch.com/zh_cn/Login/DoLogin"

    params ={
        "UserNameInput" : "MgjIpTjWp6SBKvYQSdKNNWaJT3w0W8JVEX53OBUGM9C1l0i/Pzl+vDbKx2TI4VxINOQeOfGiGOHAReCabYtxTJ3Zdu148qM00+WvO/7cXqHMsDbIGaEkrmlYTMjhcC13BgU1OVfHpGmErsC7bGDGXg5w8rNX7KshUN5/catI6uc=",
        "PasswordInput" : "OvRXgYeZqipyEXofRZ4ho22OXapIbR5Diuc46aqJImorz3y/ULsytrwqxy0CvCsSr1IH0HRNfzVUfbgrz//hzZJvkTRuqZgpX0OubgGff0ZNydBnsJchu5xmQPoXpbo+esCGocJ2i4pHtHpbjODujA2FBvpKW3MJw8YuIQ2+R3w=",
        "IsKeepLoginState" : "false",
        "geetest_challenge" :_challenge,
        "geetest_validate" : _validate,
        "geetest_seccode" :_validate + "|jordan"
    }

    params = urlencode(params)
    req = urllib2.Request(url,params)

    if m =="POST":
        f = urllib2.urlopen(req)
    else:
        f=urllib2.urlopen(req)
    content = f.read()
    res = json.loads(content)

    print res


if __name__ == '__main__':
    main()
