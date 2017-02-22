# add an import at the top:
from .security import EntryFactory

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # ... Add the factory keyword argument to our route configurations:
    config.add_route('home', '/', factory=EntryFactory)
    config.add_route('detail', '/journal/{id:\d+}', factory=EntryFactory)
    config.add_route('action', '/journal/{action}', factory=EntryFactory)
    config.add_route('auth', '/sign/{action}', factory=EntryFactory)
