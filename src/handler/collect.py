#! /usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import simplejson as json
import redis
import uuid


class CiaCollectdHandler(tornado.web.RequestHandler):

    @property
    def redis_conn(self):
        return redis.Redis(host='127.0.0.1', port=6379)

    def get(self):
        self.post()

    def post(self):
        try:
            print self.request.remote_ip, self.request.headers['X-Real-IP'], self.request.body

            alexa = json.loads(self.request.body)

            # params
            uuid_str = uuid.uuid1()
            self.redis_conn.hset(uuid_str, "cdt", alexa['cdt'])
            self.redis_conn.hset(uuid_str, "url", alexa['url'])
            self.redis_conn.hset(uuid_str, "ref", alexa['ref'])
            self.redis_conn.expire(uuid_str, 3600)

            # worker
            self.redis_conn.lpush("alexa_robot_worker", uuid_str)

            # print headers,body
        except Exception, e:
            print e
