#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import urllib
import httplib2

# 换成要替换的url 根目录时后面要添加下划线
TARGET_URL = "http://atschx.com/"
# DATA_ALEXA_URL = "https://data.alexa.com/data/%s?%s&cdt=%s&ref=%s&url=%s"
DATA_ALEXA_URL = "https://data.alexa.com/data/%s?%s&%s"


def gen_url():
    aid = redis_conn.srandmember("alexa_aid_pool")
    seed = redis_conn.lpop("alexa_robot_worker")

    if seed is not None:
        cdt = redis_conn.hget(seed, "cdt")
        ref = redis_conn.hget(seed, "ref")
        url = redis_conn.hget(seed, "url")

        # base = "cli=10&ver=alxg-3.3&dat=ns"
        base = "cli=10&ver=alxf-3.0.1&dat=ns"

        if cdt is not None and ref is not None and url is not None:
            url = TARGET_URL
            query_str = {"cdt": cdt, "url": url, "ref": ref}
            # base = "cli=10&ver=alxg-3.3&dat=ns"
            if aid is not None:
                # data_url = DATA_ALEXA_URL % (aid, base, cdt, ref, TARGET_URL)
                data_url = DATA_ALEXA_URL % (aid, base, urllib.urlencode(query_str))
                return data_url


def send_request(uri=None):
    conn = httplib2.Http()
    headers = {
        # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36
        # (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0"
    }
    if uri is not None:
        print uri
        # uri = "https://data.alexa.com/data?cli=10&stc"
        resp, content = conn.request(uri, "GET", None, headers)
        # print json.dumps(resp)
        if resp['status'] == '200' and resp['content-type'] == 'text/xml':
            print content
            return content

if __name__ == '__main__':
    redis_conn = redis.Redis(host='127.0.0.1', port=6379)
    queue = redis_conn.llen("alexa_robot_worker")
    print queue
    if queue is not None:
        for i in range(queue):
            send_request(gen_url())
