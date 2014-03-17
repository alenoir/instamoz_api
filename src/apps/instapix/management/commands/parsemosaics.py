from django.core.management.base import BaseCommand

from src.apps.instapix.models import Mosaic


class Command(BaseCommand):
    help = 'Parse mosaics'

    def handle(self, *args, **options):
        self.stdout.write('Begin parse mosaic')        
                
        for mosaic in Mosaic.objects.filter(is_parse=False):
            self.stdout.write('>>> Parse mosaic %s' % mosaic.name)
            mosaic.parse_pixesl()
                    
                    
            