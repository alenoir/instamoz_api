import struct

from PIL import Image

from django.core.management.base import BaseCommand
from instapix.models import Mosaic, Pixel
from django.conf import settings

class Command(BaseCommand):
    help = 'Parse mosaics'

    def handle(self, *args, **options):
        self.stdout.write('Begin parse mosaic')        
                
        for mosaic in Mosaic.objects.filter(is_parse=False):
            self.stdout.write('>>> Parse mosaic %s' % mosaic.name)
            mosaic.parse_pixesl()
                    
                    
            