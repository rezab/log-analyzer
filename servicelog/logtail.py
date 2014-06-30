#!/usr/bin/env python
# Author: Reza Bakhshayeshi
# Email: reza.b2008 [at] gmail [dot] com
# Version: 0.3

import tornado.websocket
import os
from tornado.options import parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import wsgi

LISTENERS = []
FILENAME = ''


class TailHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened!"
        LISTENERS.append(self)

    def on_message(self, message):
        print "Message received!"
        global FILENAME
        FILENAME = message
        global tailed_file
        tailed_file = open(FILENAME)
        tailed_file.seek(os.path.getsize(FILENAME))

    def on_close(self):
        print "WebSocket closed!"
        try:
            LISTENERS.remove(self)
            tailed_file.close()
            global FILENAME
            FILENAME = ''
        except:
            pass


def check_file():
    if FILENAME != '':
        where = tailed_file.tell()
        line = tailed_file.readline()
        if not line:
            tailed_file.seek(where)
        else:
            print "File refresh"
            for element in LISTENERS:
                element.write_message(line)
    else:
        pass


class Application(tornado.web.Application):
    def __init__(self):
        wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
        handlers = [
            (r'/tail/', TailHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ]
        settings = {
            'template_path': 'templates',
            'static_path': 'static',
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8001)
    tailed_callback = tornado.ioloop.PeriodicCallback(check_file, 500)
    tailed_callback.start()
    io_loop = tornado.ioloop.IOLoop.instance()
    try:
        io_loop.start()
    except SystemExit, KeyboardInterrupt:
        io_loop.stop()
        tailed_file.close()
