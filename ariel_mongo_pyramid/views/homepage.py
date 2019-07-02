from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from ..db.video import Video


@view_defaults(route_name="homepage", renderer="ariel_mongo_pyramid:templates/home.pt")
class homepage:
    def __init__(self, request):
        self.request = request

    def update_videos(self):
        videos = []
        for video in Video.objects:
            videos.append(video.to_mongo().to_dict())

        self.request.session['videos'] = videos

    def get_videos(self):
        session = self.request.session
        return session.get("videos", [])

    @view_config()
    def homepage(self):
        self.update_videos()
        videos = self.get_videos()
        return {'videos': videos}

    @view_config(request_method='POST', request_param='form.create')
    def create(self):
        params = self.request.params
        video = Video(name=params['name'], theme=params['theme'])
        video.save()
        self.update_videos()
        videos = self.request.session.get("videos", [])
        return {'message': "Video Created!", 'videos': videos}

    @view_config(request_method='POST', request_param='thumbs_up')
    def thumbs_up(self):
        params = self.request.params
        video = Video.objects.get(id=params['_id'])
        video['thumbs_up'] = video['thumbs_up'] + 1
        video.save()
        self.update_videos()

        videos = self.request.session.get("videos", [])
        return {'videos': videos}

    @view_config(request_method='POST', request_param='thumbs_down')
    def thumbs_down(self):
        params = self.request.params
        video = Video.objects.get(id=params['_id'])
        video['thumbs_down'] = video['thumbs_down'] + 1
        video.save()
        self.update_videos()

        videos = self.request.session.get("videos", [])
        return {'videos': videos}
