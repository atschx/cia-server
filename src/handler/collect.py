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
            print self.request.remote_ip, self.request.body

            self.redis_conn.sadd("alexa_ip_pool", self.request.headers['X-Real-IP'])
            self.redis_conn.sadd("alexa_ua_pool", self.request.headers['User-Agent'])

            # params
            alexa = json.loads(self.request.body)
            uuid_str = uuid.uuid1()
            self.redis_conn.hset(uuid_str, "cdt", alexa['cdt'])
            self.redis_conn.hset(uuid_str, "url", alexa['url'])
            self.redis_conn.hset(uuid_str, "ref", alexa['ref'])
            self.redis_conn.expire(uuid_str, 86400)

            # worker
            self.redis_conn.lpush("alexa_robot_worker", uuid_str)
            self.redis_conn.expire(uuid_str, 86400)

        except Exception, e:
            print e
