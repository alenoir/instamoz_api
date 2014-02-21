import Image
import struct

from django.core.management.base import BaseCommand
from instapix.models import Mosaic, Pixel
from django.conf import settings
from instagram.client import InstagramAPI

class Command(BaseCommand):
    def handle(self, *args, **options):
        for mosaic in Mosaic.objects.all():
            img = Image.new('RGB',(620,620), "white")
            for pixel in mosaic.pixels.filter(pic__isnull=False):
                filepath = settings.MEDIA_ROOT + '/pics/%s_%s.jpg' % (mosaic.pixel_size,pixel.pic.id)
                
                print '-------------'
                print pixel.pic.id
                print mosaic.pixel_size
                print pixel.x
                print pixel.y
                print '-------------'
                try:
                    img.paste(Image.open(filepath), (pixel.y,pixel.x))
                except:
                    #pixel.pic.delete()
                    pass

            out_path = settings.MEDIA_ROOT + '/mosaic/bg_%s.jpg' % mosaic.id
            img.save(out_path)