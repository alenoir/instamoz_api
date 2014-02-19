import Image
import struct

from django.core.management.base import BaseCommand
from instapix.models import Mosaic, Pixel, InstaPic
from django.conf import settings
from instagram.client import InstagramAPI

class Command(BaseCommand):
    help = 'Associate instagram image with pixels'

    def handle(self, *args, **options):
        self.stdout.write('Begin fetch Instagram pics')
                
        for instapic in InstaPic.objects.filter(pixels__isnull=True)[0:100]:
            self.stdout.write('>>> Parse pic %s' % instapic.id)
            instapic.find_related_pixel()
            