from pyramid.response import FileResponse
from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def aboutme(request):
    return FileResponse('about/aboutme.html', request=request, content_type='text/html')
def index(request): 
    return FileResponse('index.html', request=request, content_type='text/html')

if __name__ == '__main__':
    conf = Configurator()
    conf.add_view(index, route_name='index')
    conf.add_view(aboutme, route_name='aboutme')
    conf.add_route("index",'/')
    conf.add_route('aboutme', 'about/aboutme.html')
    server = make_server('127.0.0.1', 8000, conf.make_wsgi_app())
    server.serve_forever()
