#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
# import redis
# import datetime

'''
1. fetch aid from data.alexa.com
2. send_request to data.alexa.com use get
3. random compose
'''

AID_GEN_URL = "https://data.alexa.com/data?cli=10&stc"


def gen_aid():
    """
    模拟生成aid,注意事项:
    1.发送请求时的ua
    2.server返回的Header中`Set-cookie`信息
    """
    print '发送GET请求到{%s}获取aid' % AID_GEN_URL
    # xml 解析处理
    print "获取"


def send_request(url):
    buff = urllib2.open(url)
    result = buff.open(url).read()
    buff.close()
    print "发送数据到data.alexa.com，返回％s" % result

if __name__ == '__main__':

    # full mode
    # https://data.alexa.com/data/
    # 0GgHm1BdRkC1f4?
    # cli=10&ver=alxg-3.3&dat=ns(依据浏览器存在部分差异)
    # &cdt=rq%3D0%26wid%3D723%26t%3D0%26ss%3D1280x800%26bw%3D1152%26winid%3D598%26cttl%3D709%26m%3DGET%26s%3D200
    # &ref=
    # &url=https%3A%2F%2Fwww.baidu.com%2FZmbNdvlpVkaee%2BOddQzH2Q%3D%3D%23anonymous
    # Headers
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
    # Cookie: 
    # __auc=688944c815292faf67adab26903; 
    # _ga=GA1.2.1025565774.1454164869; 
    # lv=1454601411; 
    # tbver=alxg-3.3; 
    # aid=0GgHm1BdRkC1f4
    # AlexaToolbar-ALX_NS_PH: AlexaToolbar/alxg-3.3

    # https://data.alexa.com/data/%s?%s&cdt=%s&ref=%s&url=%s
    # %s aid
    # %s base
    # %s cdt
    # %s ref
    # %s url

    # '''
    # 基础参数部分：
    #     chrome:cli＝10&ver＝alxg-3.3&dat=ns
    #     firefox:cli＝10&ver＝alxg-3.3&dat=ns
    # cdt参数部分
    #     rq: 同一个tab页打开本页面的次数
    #     wid: 打开当前页面的tabId
    #     t: 0|1 根据referer决定 payload.referer ? "1" : "0"
    #     ss：屏幕分辨率
    #     bw：窗口宽度
    #     winid：这个是tabId所在的windowId
    #     cttl: 页面load时间 window.performance.timing.domContentLoadedEventEnd-window.performance.timing.navigationStart,
    #     m: 可选 打开网站的方法 method 填GET即可
    #     s: http状态码 200 即可 
    # 待更新的url
    #     ref= payload.referer ? encodeURIComponent( payload.referer )
    #     url＝inurl ? encodeURIComponent( inurl )
    # '''

    # redis_conn = redis.Redis(host='127.0.0.1', port=6379)
    ua="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"


    # cli="10"
    # ver="alxg-3.3"
    # dat="ns"
    # cdt=buildCDT()
    # ref=""
    # url="http://atschx.com"

    queryStr = {'cli':cli,'dat':dat,'cdt':cdt,'ref':ref,'url':url}

    alexa_data_url= baseline % urllib.urlencode(queryStr)
    print alexa_data_url
    # sendRequest(alexa_data_url)

    #1.AID 池子数据 替换0GgHm1BdRkC1f4


