#! /usr/bin/env python
#-*- coding: utf-8 -*- 
from handler.collect import UserActionCollectHandler 

import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.web
import config
import logging
import signal
import os.path

# define("mid", default="1", help="Machine id")
# define("port", default=4000, help="port to run")
# define("notifylog", help="notify log file")
# define("debug", default=True, help="is debug model?", type=bool)

'''
test
'''
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/collectd',UserActionCollectHandler)]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'web')
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    # signal.signal(signal.SIGTERM,onsignal_term)    
    # options.parse_command_line()
    # init_logging(options)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(4000)
    ioloop = tornado.ioloop.IOLoop.instance()
    # if config.debug:
    #     tornado.autoreload.start(ioloop)
    # logging.info('server listen at %d', options.port)
    ioloop.start()

if __name__ == '__main__':
    main();