def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # routes are attempted in order - takes first success
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('action', '/journal/{action}')
