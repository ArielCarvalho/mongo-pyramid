from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from operator import itemgetter
from ..db.video import Video


@view_defaults(route_name="theme_score", renderer="ariel_mongo_pyramid:templates/theme_score.pt")
class theme_score:
    def __init__(self, request):
        self.request = request

    @view_config()
    def theme_score(self):
        t = {}
        for video in Video.objects:
            v_dict = video.to_mongo().to_dict()

            theme = t.get(v_dict['theme'], 0)
            if theme:
                new_up = theme.get('up', 0) + v_dict['thumbs_up']
                new_down = theme.get('down', 0) + v_dict['thumbs_down']
            else:
                new_up = v_dict['thumbs_up']
                new_down = v_dict['thumbs_down']

            t[v_dict['theme']] = {
                'name': v_dict['theme'],
                'up': new_up,
                'down': new_down,
                'score': new_up - (new_down / 2)
            }

        themes = []
        for key, value in t.items():
            themes.append(value)

        return {'themes': sorted(themes, key=itemgetter('score'), reverse=True)}
