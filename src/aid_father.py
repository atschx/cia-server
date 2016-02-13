#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
import redis


class AidGenerator(object):
    """
    just for test
    """

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
        finally:
            print name, str(attrs)

if __name__ == '__main__':

    xml = r'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Need more Alexa data?  Find our APIs here: https://aws.amazon.com/alexa/ -->
<ALEXA VER="0.9" URL="404" HOME="0" AID="7JlHm1B95im3gL" IDN="">
</ALEXA>
'''
    parser = ParserCreate()
    parser.StartElementHandler = AidGenerator().extra_aid_to_redis
    parser.Parse(xml)

