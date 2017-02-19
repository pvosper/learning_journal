from pyramid.response import Response
from pyramid.view import view_config


# from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound
from .forms import EntryCreateForm

# from ..models import Entry

from ..models.mymodel import Entry, DBSession # <- Add this import

from pyramid.httpexceptions import HTTPNotFound

# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(Entry)
#         one = query.filter(Entry.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'learning_journal'}

# http://localhost:6543

@view_config(route_name='home', renderer='templates/list.jinja2')
def index_page(request):
    entries = Entry.all()
    return {'entries': entries}
    # return 'list page'

# http://localhost:6543/journal/1

@view_config(route_name='detail', renderer='templates/detail.jinja2')
def view(request):
    this_id = request.matchdict.get('id', -1)
    entry = Entry.by_id(this_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}

# http://localhost:6543/journal/create

@view_config(route_name='action', match_param='action=create',
             renderer='templates/edit.jinja2')
def create(request):
    entry = Entry()
    form = EntryCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}

# http://localhost:6543/journal/edit

@view_config(route_name='action', match_param='action=edit',
             renderer='templates/edit.jinja2')
def update(request, id):
    entry = Entry.by_id(id)
    if not entry:
        return HTTPNotFound()
    # return page
    return {'entry': entry}
    # return 'edit page'


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:
1.  You may need to run the "initialize_learning_journal_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.
2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
After you fix the problem, please restart the Pyramid application to
try it again.
"""