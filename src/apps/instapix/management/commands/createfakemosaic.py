import Image
from django.core.management.base import BaseCommand
from django.conf import settings

from src.apps.instapix.models import Mosaic


class Command(BaseCommand):
    def handle(self, *args, **options):
        for mosaic in Mosaic.objects.all():
            img = Image.new('RGB',(620,620), "white")
            for pixel in mosaic.pixels.filter(pic__isnull=False):
                try:
                    print '-------------'
                    print pixel.id
                    print mosaic.pixel_size
                    filepath = settings.MEDIA_ROOT + '/pics/%s_%s.jpg' % (mosaic.pixel_size,pixel.pic.id)
                    
                    
                    print pixel.x
                    print pixel.y
                    print '-------------'
                    try:
                        img.paste(Image.open(filepath), (pixel.y,pixel.x))
                    except:
                        #pixel.pic.delete()
                        pass
                except:
                    pass

            out_path = settings.MEDIA_ROOT + '/mosaic/bg_%s.jpg' % mosaic.id
            img.save(out_path)