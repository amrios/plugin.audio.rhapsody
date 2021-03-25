from .metadata import *


class Tracks(MetadataList, MetadataDetail):
    class Base(object):
        def __init__(self, data):
            self.id = data['id']
            self.name = data['name']
            try:
                self.duration = data['duration']
            except KeyError:
                try:
                    self.duration = data['playbackSeconds']
                except KeyError:
                    self.duration = None

    class List(Base):
        def __init__(self, data):
            from . import albums
            from . import artists

            super(Tracks.List, self).__init__(data)
            self.artist = artists.Artists.Base(data['artist'])
            self.album = albums.Albums.Base(data['album'])

    class Detail(List):
        def __init__(self, data):
            super(Tracks.Detail, self).__init__(data)

    url_base = 'tracks'
    list_class = List
    detail_class = Detail

    def top(self):
        return self.list('top')
