#! /usr/bin/env python
# -*- coding: utf-8 -*-

from handler.collect import CiaCollectdHandler

import tornado.ioloop
import tornado.web

application = tornado.web.Application([
    (r'/collectd', CiaCollectdHandler),
])


def main():
    application.listen(4000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()