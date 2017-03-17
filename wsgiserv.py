from wsgiref.simple_server import make_server

class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        for strng in self.app(environ, start_response):
            if strng.find('<body>') > 0: 
		yield strng.encode() + "<div class='top'>Middleware TOP</div>".encode()
            elif strng.find('</body>') > 0: 
		yield "<div class='bottom'>Middleware BOTTOM</div>".encode() + strng.encode()
            else: 
		yield strng.encode()
				
def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/HTML')])
    file = open(environ['PATH_INFO'], 'r')
    return file				
				
server = make_server('127.0.0.1', 8000, Middleware(app))
server.serve_forever()
