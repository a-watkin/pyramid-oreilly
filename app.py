from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home_page', renderer='home.jinja2')
def home(request):
  return dict(site_name='MyApp')


@view_config(route_name='hello', renderer='hello_world.jinja2')
def hello_world(request):
  return dict(name='world')


@view_config(route_name='hello', renderer='hello_name.jinja2',
              request_param='name')
def hello_name(request):
  name = request.params.get('name')
  return dict(name=name)


# start by just running it with python app.py
if __name__ == "__main__":
  config = Configurator()
  config.include('pyramid_jinja2')
  config.add_route('home_page', '/')
  config.add_route('hello', '/hello')
  # config.add_view(hello, route_name='hello_world')

  # finds view_config
  config.scan()
  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6543, app)
  print('Serving at http://127.0.0.1:6543')
  server.serve_forever()