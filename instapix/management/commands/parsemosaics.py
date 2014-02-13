import struct

from PIL import Image

from django.core.management.base import BaseCommand
from instapix.models import Mosaic, Pixel
from django.conf import settings

class Command(BaseCommand):
    help = 'Parse mosaics'

    def handle(self, *args, **options):
        self.stdout.write('Begin parse mosaic')
         
        # conf
        pixelSize = 10
        middlePixel = pixelSize/2
                
        for mosaic in Mosaic.objects.all():
            self.stdout.write('>>> Parse mosaic %s' % mosaic.name)
            image = Image.open(mosaic.image.path)
            pixels = list(image.getdata())
            width, height = image.size
            self.stdout.write('width : %s' % width)
            self.stdout.write('height : %s' % height)
            pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
            
            i=middlePixel
            coorX=middlePixel
            while i < width:
                
                if i<width:
                    j=middlePixel
                    coorY=middlePixel
                    while j < height:
                        
                        if j<height:
                            
                            hexaColor = struct.pack('BBB',*pixels[i][j]).encode('hex')
                            try:
                                pix = Pixel.objects.get(x=coorX,y=coorY,mosaic=mosaic)
                            except Pixel.DoesNotExist:
                                self.stdout.write('Add pixel %s,%s' % (coorX, coorY))
                                pix = Pixel.objects.create(x=coorX,y=coorY,mosaic=mosaic)
                                
                            self.stdout.write('Update pixel %s,%s with color : %s' % (coorX, coorY, hexaColor))
                            pix.color = hexaColor
                            pix.save()
                        j=j+pixelSize
                        coorY=coorY+pixelSize
                i=i+pixelSize
                coorX=coorX+pixelSize
                    
                    
            