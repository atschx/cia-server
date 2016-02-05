#! /usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import simplejson as json
import redis


class UserActionCollectHandler(tornado.web.RequestHandler):

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            body = self.request.body
            alexa = json.loads(body)
            print alexa['cdt'], alexa['ref'], alexa['url']
            print "---------------------------------------"
            # print headers,body
        except Exception , e:
            print e
