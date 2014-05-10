from django.core.management.base import BaseCommand

from instamoz.apps.instapix.models import InstaPic


class Command(BaseCommand):
    help = 'Associate instagram image with pixels'

    def handle(self, *args, **options):
        self.stdout.write('Begin fetch Instagram pics')
                
        for instapic in InstaPic.objects.filter(pixels__isnull=True).filter(is_parse=False)[0:100]:
            self.stdout.write('>>> Parse pic %s' % instapic.id)
            instapic.find_related_pixel()
            