from .metadata import *


class Image(MetadataDetail.Detail, object):
    TYPE_ARTIST = 'http://direct.rhapsody.com/imageserver/v2/artists/{0:s}/images/{1:s}.{2:s}'
    TYPE_ALBUM = 'http://direct.rhapsody.com/imageserver/v2/albums/{0:s}/images/{1:s}.{2:s}'
    TYPE_PLAYLIST = 'http://direct.rhapsody.com/imageserver/v2/playlists/{0:s}/artists/images/{1:s}.{2:s}'
    TYPE_GENRE = 'http://direct.rhapsody.com/imageserver/images/{0:s}/{1:s}.{2:s}'
    TYPE_IMAGESET = 'http://direct.rhapsody.com/imageserver/v2/imagesets/{0:s}/images/{1:s}.{2:s}'
    TYPE_STATION = 'http://direct.rhapsody.com/imageserver/v2/stations/{0:s}/images/{1:s}.{2:s}'

    SIZE_ARTIST_TINY = '70x47'
    SIZE_ARTIST_SMALL = '150x100'
    SIZE_ARTIST_MEDIUM = '356x237'
    SIZE_ARTIST_LARGE = '633x422'
    SIZE_ARTIST_ORIGINAL = '1800x600'

    SIZE_ALBUM_TINY = '70x70'
    SIZE_ALBUM_SMALL = '170x170'
    SIZE_ALBUM_MEDIUM = '200x200'
    SIZE_ALBUM_LARGE = '300x300'
    SIZE_ALBUM_ORIGINAL = '500x500'

    SIZE_PLAYLIST_MEDIUM = '230x153'
    SIZE_PLAYLIST_LARGE = '1200x400'
    SIZE_PLAYLIST_ORIGINAL = '1800x600'

    SIZE_GENRE_SMALL = '161x64'
    SIZE_GENRE_MEDIUM = '240x160'
    SIZE_GENRE_ORIGINAL = '1800x600'

    SIZE_IMAGESET_TINY = '70x70'
    SIZE_IMAGESET_SMALL = '170x170'
    SIZE_IMAGESET_MEDIUM = '200x200'
    SIZE_IMAGESET_LARGE = '300x300'
    SIZE_IMAGESET_ORIGINAL = '500x500'

    SIZE_STATION_TINY = '70x70'
    SIZE_STATION_SMALL = '170x170'
    SIZE_STATION_MEDIUM = '200x200'
    SIZE_STATION_LARGE = '300x300'
    SIZE_STATION_ORIGINAL = '1800x600'

    FORMAT_JPEG = 'jpg'
    FORMAT_PNG = 'png'

    def __init__(self, data):
        super(Image, self).__init__(data)
        self.width = data['width']
        self.height = data['height']
        self.url = data['url']

    @staticmethod
    def get_url(image_type, image_id, image_size, image_format=FORMAT_JPEG):
        return image_type.format(image_id, image_size, image_format)
