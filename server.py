import tornado.web
import tornado.ioloop

from int_to_numeral import int_to_numeral



class MainHandler(tornado.web.RequestHandler):
    def get(self, integer_uri):
        integer = self.request.uri.split('/')[1]
        integer = int(integer)
        numeral = int_to_numeral(integer)
        payload = {"extenso": numeral}
        self.write(payload)




if __name__=='__main__':
    application = tornado.web.Application([
        (r"/[-]?([0-9]){1,5}", MainHandler),
    ])
    application.listen(3000)
    tornado.ioloop.IOLoop.current().start()

