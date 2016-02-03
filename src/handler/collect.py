#! /usr/bin/env python
#-*- coding: utf-8 -*- 

import  tornado.web
import simplejson as json
import urllib

class UserActionCollectHandler(tornado.web.RequestHandler):

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            body = self.request.body
            print body
        except Exception , e:
            print e