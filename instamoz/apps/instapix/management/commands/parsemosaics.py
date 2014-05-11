from PIL import Image
from django.core.management.base import BaseCommand
from django.conf import settings

from instamoz.apps.instapix.models import Mosaic


class Command(BaseCommand):
    help = 'Parse mosaics'

    def handle(self, *args, **options):
        self.stdout.write('Begin parse mosaic')        
                
        for mosaic in Mosaic.objects.filter(is_parse=False):
            self.stdout.write('>>> Parse mosaic %s' % mosaic.name)
            mosaic.parse_pixesl()

            img = Image.new('RGB',(620,620), "white")
            out_path = settings.MEDIA_ROOT + '/mosaic/bg_%s.png' % mosaic.id
            img.save(out_path, "PNG")
                    
                    
            