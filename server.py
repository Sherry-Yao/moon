#!/usr/bin/env python
# encoding: utf-8

import tornado.ioloop
import tornado.web
import tornado.httpserver
import sys
from application import Application

#Python2.5初始化后会删除sys.setdefaultencoding, 重新载入
reload(sys)
sys.setdefaultencoding('utf-8')

#servername: 127.0.0.1
#port: 8000
from tornado.options import define, options
define("port", default=8000, help="run in given port", type=int)

if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    print "Server Start Successfully!"
    tornado.ioloop.IOLoop.instance().start()
