from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

Status = '200 OK'

def app(environ, start_response):
    start_response(Status, [('Content-Type', 'text/html')])
    PATH = environ['PATH_INFO']
    return [Environment(loader=FileSystemLoader('templates')).get_template(PATH).render(link=PATH).encode('utf-8')]

if name == '__main__':
     server = make_server('127.0.0.1', 8000, app)
     server.serve_forever()
