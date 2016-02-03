#! /usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import simplejson as json


class UserActionCollectHandler(tornado.web.RequestHandler):

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            body = self.request.body
            # json.loads(body)
            print body
            # print headers,body
        except Exception , e:
            print e
