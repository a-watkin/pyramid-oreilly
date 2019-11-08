from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, notfound_view_config

# pyramid finds the class instantiated it then finds the method to use
# the instance of the class is then available in the view template

# you can also decorate entire classes for things like auth
class MySite:
  def __init__(self, request):
    self.request = request
  
  # Extracts some info in the request
  # makes it available as an attribute in the view instance
  # so you can call is as view.current from the template

  # this is a helper method
  @property
  def current(self):
    return self.request.matchdict.get('id')

  @view_config(route_name='list', renderer='templates/list.jinja2')
  def list(self):
    return dict()

  @view_config(route_name='add', renderer='templates/add.jinja2')
  def add(self):
    return dict()

  @view_config(route_name='view', renderer='templates/view.jinja2')
  def view(self):
    current = self.request.matchdict.get('id')
    return dict(current=current)


  @view_config(route_name='edit', renderer='templates/edit.jinja2')
  def edit(self):
    current = self.request.matchdict.get('id')
    return dict(current=current)

  @view_config(route_name='edit', renderer='templates/edit.jinja2', request_method='POST')
  def edit_handler(self):
    # Getting the params from the form?
    new_title = self.request.params.get('new_title')
    print('New title ', new_title)
    # Redirecting after post to another view.
    url = self.request.route_url('list')
    return HTTPFound(url)


  @view_config(route_name='delete', renderer='templates/delete.jinja2')
  def delete(self):
    url = self.request.route_url('list')
    # Redirects.
    return HTTPFound(url)