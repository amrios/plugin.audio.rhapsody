from .metadata import *


class Genres(MetadataList, MetadataDetail):
    class Base(object):
        def __init__(self, data):
            self.id = data['id']
            self.name = data['name']

    class List(Base):
        def __init__(self, data):
            super(Genres.List, self).__init__(data)
            self.subgenres = [Genres.List(x) for x in data.get('subgenres', [])]

    class Detail(Base):
        def __init__(self, data):
            super(Genres.Detail, self).__init__(data)

    url_base = 'genres'
    list_class = List
    detail_class = Detail

    def find(self, genre_id, genre_list=None):
        if genre_list is None:
            genre_list = self.list()
        for genre in genre_list:
            if genre.id == genre_id:
                return genre
            sub = self.find(genre_id, genre_list=genre.subgenres)
            if sub is not None:
                return sub

    def top_artists(self, genre_id):
        from rhapsody.models import artists
        return self.list(genre_id + '/artists/top', artists.Artists.List)

    def top_albums(self, genre_id):
        from rhapsody.models import albums
        return self.list(genre_id + '/albums/top', albums.Albums.List)

    def top_tracks(self, genre_id):
        from rhapsody.models import tracks
        return self.list(genre_id + '/tracks/top', tracks.Tracks.List)

    def new_albums(self, genre_id):
        from rhapsody.models import albums
        return self.list(genre_id + '/albums/new', albums.Albums.List)

    def stations(self, genre_id):
        from rhapsody.models import stations
        return self.list(genre_id + '/stations', stations.Stations.List)
