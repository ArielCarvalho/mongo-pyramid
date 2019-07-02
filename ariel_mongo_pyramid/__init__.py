from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):

    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(
        settings=settings, session_factory=my_session_factory)

    config.add_settings({"mongodb_name": "Ariel_mongo_pyramid_interview"})

    config.include('pyramid_chameleon')
    config.include("pyramid_mongoengine")
    config.add_connection_database()

    config.add_static_view(name='static', path='ariel_mongo_pyramid:static')

    config.add_route("homepage", "/")
    config.add_route("theme_score", "/theme_score")

    config.scan('.views')
    return config.make_wsgi_app()
