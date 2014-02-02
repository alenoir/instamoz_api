import Image
import struct

from django.core.management.base import BaseCommand
from instapix.models import Mosaic, Pixel
from django.conf import settings
from instagram.client import InstagramAPI

class Command(BaseCommand):
    help = 'Parse mosaics'

    def handle(self, *args, **options):
        self.stdout.write('Begin get Instagram pics')
                
        for mosaic in Mosaic.objects.all():
            self.stdout.write('>>> Parse mosaic %s' % mosaic.name)
            
            for tag in mosaic.tags.all():
                api = InstagramAPI(client_id='7ba882f721c4412cadb351f29ba8109f', client_secret='0d475653225f4b2188337a721d4e3a5d')
                medias, next = api.tag_recent_media(10, 0, tag)

                print medias
                for media in medias:
                    image = Image.open(media.images['standard_resolution'].url)
                    image = image.resize((150, 150))
                    result = image.convert('P', palette=Image.ADAPTIVE, colors=10)
                    result.putalpha(0)
                    colors = result.getcolors(150*150)
                    print colors
                    print media.images['standard_resolution'].url
            