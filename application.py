#!/usr/bin/env python
# encoding: utf-8

import tornado.web
import os
from handlers import *
from conf.session import SessionManager

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/play", PlayHandler),
            (r"/(.*)", IndexHandler)
        ]

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'cookie_secret': 'e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d',
            'session_secret': '3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc',
            'session_timeout': 1296000, # save for half month
            'store_option': {
                'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': ''
            },
            'debug': True
        }

        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = SessionManager( \
                settings['session_secret'], settings['store_option'], settings['session_timeout'])
