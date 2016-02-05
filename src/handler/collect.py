#! /usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import simplejson as json
import redis
import uuid


class UserActionCollectHandler(tornado.web.RequestHandler):

    def __init__(self):
        """
        redis-connect
        """
        self.redis_conn = redis.Redis(host='127.0.0.1', port=6379)
        super(UserActionCollectHandler, self).__init__()

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            body = self.request.body
            alexa = json.loads(body)
            print alexa['cdt'], alexa['url'], alexa['ref']
            print "---------------------------------------"
            uuidStr=uuid.uuid1()
            self.redis_conn.hset(uuidStr, "cdt", alexa['cdt'])
            self.redis_conn.hset(uuidStr, "url", alexa['url'])
            self.redis_conn.hset(uuidStr, "ref", alexa['ref'])
            # print headers,body
        except Exception , e:
            print e
