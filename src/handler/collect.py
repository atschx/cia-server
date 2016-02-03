#! /usr/bin/env python
#-*- coding: utf-8 -*- 

import tornado.web
import simplejson as json
import urllib

class UserActionCollectHandler(tornado.web.RequestHandler):

    def __init__(self):
        tornado.web.RedirectHandler.add_header('Content-Type', 'application/json; charset=utf-8')
        tornado.web.RedirectHandler.add_header('Cache-Control', 'no-Cache')
        tornado.web.RedirectHandler.add_header(self,'Access-Control-Allow-Origin','*')

    def get(self):
        self.post()

    def post(self):
        try:
            headers = self.request.headers
            body = self.request.body
            print headers,body
        except Exception , e:
            print e
