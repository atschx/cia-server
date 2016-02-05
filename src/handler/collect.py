#! /usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import simplejson as json
import redis
import uuid


class UserActionCollectHandler(tornado.web.RequestHandler):

    @property
    def redis_conn(self):
        return redis.Redis(host='127.0.0.1', port=6379)

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            print headers
            body = self.request.body
            alexa = json.loads(body)
            print alexa['cdt'], alexa['url'], alexa['ref']
            print "---------------------------------------"
            uuid_str=uuid.uuid1()
            self.redis_conn.hset(uuid_str, "cdt", alexa['cdt'])
            self.redis_conn.hset(uuid_str, "url", alexa['url'])
            self.redis_conn.hset(uuid_str, "ref", alexa['ref'])
            # print headers,body
        except Exception, e:
            print e
