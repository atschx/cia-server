#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
robot :
1. 随机组合参数
2. 生成alexa的请求URL
3. 提交task到celery
"""

import redis
import urllib
import random
from tasks import send_to_alexa
# DATA_ALEXA_URL = "https://data.alexa.com/data/%s?%s&cdt=%s&ref=%s&url=%s"
DATA_ALEXA_URL = "https://data.alexa.com/data/%s?%s&%s"


def gen_url():
    aid = redis_conn.srandmember("alexa_aid_pool")
    seed = redis_conn.lpop("alexa_robot_worker")

    if seed is not None:
        cdt = redis_conn.hget(seed, "cdt")
        ref = redis_conn.hget(seed, "ref")
        url = redis_conn.hget(seed, "url")

        base = random.sample(BASES, 1)[0]

        if cdt is not None and ref is not None and url is not None:
            url = random.sample(TARGET_URLS, 1)[0]
            query_str = {"cdt": cdt, "url": url, "ref": ref}
            if aid is not None:
                # data_url = DATA_ALEXA_URL % (aid, base, cdt, ref, TARGET_URL)
                data_url = DATA_ALEXA_URL % (aid, base, urllib.urlencode(query_str))
                return data_url

if __name__ == '__main__':

    BASES = set(["cli=10&ver=alxf-3.0.1&dat=ns", "cli=10&ver=alxg-3.3&dat=ns"])

    HEADERS = {
        "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alxg-3.3",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0"
    }

    TARGET_URLS = set(["http://ghost.atschx.com/",
                       "http://ghost.atschx.com/tag/vps/",
                       "http://ghost.atschx.com/vps-start/",
                       "http://ghost.atschx.com/speed-up-backend-programming-with-go/",
                       "http://ghost.atschx.com/log-analytics/",
                       "http://blog.atschx.com/?p=489",
                       "http://blog.atschx.com/",
                       "http://blog.atschx.com/?cat=38",
                       "http://atschx.com/"
                       ])

    redis_conn = redis.Redis(host='127.0.0.1', port=6379)
    queue = redis_conn.llen("alexa_robot_worker")
    if queue is not None:
        for i in range(queue):
            data = {
                "uri": gen_url(),
                "headers": HEADERS
            }
            send_to_alexa.delay(data)
    else:
        print "暂时没有待发送的数据"