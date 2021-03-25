from datetime import date
from .metadata import *


class Albums(MetadataList, MetadataDetail):
    class Base(object):
        def __init__(self, data):
            self.id = data['id']
            self.name = data['name']

    class List(Base):
        class Type:
            def __init__(self, data):
                self.id = data['id']
                self.name = data['name']

        def __init__(self, data):
            from . import common
            from . import artists

            super(Albums.List, self).__init__(data)
            self.artist = artists.Artists.List(data['artist'])
            self.type = Albums.List.Type(data['type'])
            self.images = [common.Image(x) for x in data['images']]
            self.released = data['released']

        def get_release_date(self):
            return date.fromtimestamp(self.released / 1000)

    class Detail(List):
        def __init__(self, data):
            from . import tracks

            super(Albums.Detail, self).__init__(data)
            self.tracks = [tracks.Tracks.List(x) for x in data['tracks']]

    TYPE_MAIN_RELEASE = 0
    TYPE_SINGLE_EP = 1
    TYPE_COMPILATION = 2

    url_base = 'albums'
    list_class = List
    detail_class = Detail

    def new(self):
        return self.list('new')

    def top(self):
        return self.list('top')

    def picks(self):
        return self.list('picks')

    def tracks(self, album_id):
        from rhapsody.models import tracks

        return self.list(album_id + '/tracks', model=tracks.Tracks.List)
