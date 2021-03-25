from .metadata import *


class Artists(MetadataList, MetadataDetail):
    class Base(object):
        def __init__(self, data):
            self.id = data['id']
            self.name = data['name']

        def get_station_id(self):
            return Artists.get_station_id(self.id)

    class List(Base):
        def __init__(self, data):
            super(Artists.List, self).__init__(data)

    class Detail(Base):
        def __init__(self, data):
            super(Artists.Detail, self).__init__(data)

    class Similar(object):
        def __init__(self, data):
            self.contemporaries = [Artists.Detail(x) for x in data['contemporaries']]
            self.followers = [Artists.Detail(x) for x in data['followers']]
            self.influencers = [Artists.Detail(x) for x in data['influencers']]
            self.related = [Artists.Detail(x) for x in data['related']]

    url_base = 'artists'
    list_class = List
    detail_class = Detail

    def top(self):
        return self.list('top')

    def albums(self, artist_id):
        from . import albums

        return self.list(artist_id + '/albums', limit=1000, model=albums.Albums.List)

    def similar(self, artist_id):
        return self.detail(artist_id + '/similar', model=Artists.Similar)

    @staticmethod
    def get_station_id(artist_id):
        return artist_id.lower().replace('art.', 'sas.')
