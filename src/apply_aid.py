#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
import redis
import httplib2
import json
import time


class AidGenerator(object):

    @property
    def redis_conn(self):
        return redis.Redis(host='127.0.0.1', port=6379)

    """
    ALEXA AID xml handler.
    """
    def extra_aid_to_redis(self, name, attrs):
        """
        :param name:
        :param attrs:
        :return: 元组数据
        """
        try:
            aid = attrs['AID']
            if aid is not None:
                self.redis_conn.sadd("alexa_aid_pool", attrs['AID'])
                    # setnx("alexa_aid_pool", attrs['AID'])
        finally:
            print name, str(attrs)


def get_aid():
    conn = httplib2.Http()
    headers = {
        # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36
        # (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0"
    }
    uri = "https://data.alexa.com/data?cli=10&stc"
    resp, content = conn.request(uri, "GET", None, headers)
    print json.dumps(resp)
    if resp['status'] == '200' and resp['content-type'] == 'text/xml':
        print content
        return content

if __name__ == '__main__':
    for i in range(10):
        print "__________________________________________________________"
        xml = get_aid()
        parser = ParserCreate()
        parser.StartElementHandler = AidGenerator().extra_aid_to_redis
        parser.Parse(xml)
        time.sleep(2)
