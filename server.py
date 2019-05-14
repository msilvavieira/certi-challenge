"""
    A (very) simple, to-the-point, tornado-based http server.

    Listens to port 3000 by default, but can listen to others
    ports if started with the --port=<int> argument (as in
    "python3 server.py --port=8888").

    The MainHandler is set to accept for uris integers in the
    range [-99999, 99999], inclusive.
    
"""

import tornado.web
import tornado.ioloop
from tornado.options import define, options

from int_to_numeral import int_to_numeral



class MainHandler(tornado.web.RequestHandler):
    def get(self, integer_uri):
        integer = self.request.uri.split('/')[1]
        integer = int(integer)
        if integer > -100000 and integer < 100000:
            numeral = int_to_numeral(integer)
            payload = {"extenso": numeral}
            self.write(payload)
        else:
            raise tornado.web.HTTPError(status_code=404)



define('port', default=3000, type=int)


if __name__=='__main__':
    options.parse_command_line()
    application = tornado.web.Application([
        (r"/[-]?(\d)+", MainHandler),
    ])
    application.listen(options.port)
    try:
        tornado.ioloop.IOLoop.current().start()
    ## exit quietly with ctrl-c
    except KeyboardInterrupt as k:
        tornado.ioloop.IOLoop.current().stop()

