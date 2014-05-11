import json
import urllib, cStringIO
import struct
import os.path

from django.db import transaction
from PIL import Image
from pprint import pprint
from colormath.color_objects import RGBColor

from datetime import datetime
from django.db import models
from instagram.client import InstagramAPI
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models import Q

api = InstagramAPI(client_id=settings.INSTAGRAM_CONFIG['client_id'], client_secret=settings.INSTAGRAM_CONFIG['client_secret'])

USER_SUBSCRIPTION = 'user'
GEO_SUBSCRIPTION = 'geography'
TAG_SUBSCRIPTION = 'tag'
LOC_SUBSCRIPTION = 'location'
SUBSCRIPTION_TYPE =(
    (USER_SUBSCRIPTION, 'User'),
    (GEO_SUBSCRIPTION, 'Geographie'),
    (TAG_SUBSCRIPTION, 'Tag'),
    (LOC_SUBSCRIPTION, 'Localisation'),
    
)
class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __unicode__(self):
        return self.name

class Subscription(models.Model):
    subscription_id = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=22, choices=SUBSCRIPTION_TYPE)
    location_lat = models.FloatField(blank=True, null=True)
    location_lng = models.FloatField(blank=True, null=True)    
    radius = models.IntegerField(blank=True, null=True)    
    tag = models.ForeignKey(Tag,blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)    
    last_update = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __unicode__(self):
        return u'Type : %s, Tags : %s' % (self.type, self.tag)
    
    def clean(self):
        if self.type == GEO_SUBSCRIPTION and (self.location_lat is None or self.location_lng is None or self.radius is None):
            raise ValidationError('For goegraphy subscription, lat, lng and radius required')
        if self.type == TAG_SUBSCRIPTION and (self.tag is None):
            raise ValidationError('For atg subscription, tag required')
            
    def save(self, *args, **kwargs):
        update_sub = kwargs.pop('add_usbscription', True)
        if update_sub:
            #if self.pk is not None:
                #api.delete_subscriptions(id=self.subscription_id)
    
            if self.type == GEO_SUBSCRIPTION:
                res = api.create_subscription(object='geography', lat=self.location_lat, lng=self.location_lng, radius=self.radius, aspect='media', callback_url=settings.INSTAGRAM_CONFIG['redirect_uri'])
                self.subscription_id = res['data']['id']
                self.object_id = res['data']['object_id']
            if self.type == TAG_SUBSCRIPTION:
                res = api.create_subscription(object='tag', object_id=self.tag, aspect='media', callback_url=settings.INSTAGRAM_CONFIG['redirect_uri'])
                self.subscription_id = res['data']['id']
        else:
            self.last_update = datetime.now()
        
        return super(Subscription, self).save(*args, **kwargs)
        
    def set_last_update(self):
        self.last_update = datetime.now()
        self.save(add_usbscription=False)
    
    #@transaction.commit_on_success
    def update_subscription(self):
        self.set_last_update()

        if self.type == GEO_SUBSCRIPTION:
            recent_media, next = api.geography_recent_media(10, '', self.object_id)
 
        if self.type == TAG_SUBSCRIPTION:
            recent_media, next = api.tag_recent_media(10, '', self.tag)
        print recent_media
        for media in recent_media:
            print media.id
            if not InstaPic.objects.filter(picture_id=media.id).filter(is_parse=False).exists():
                print media.id
                                
                pic = InstaPic()
                pic.link = media.link
                pic.user_id = media.user.id
                pic.user_name = media.user.username
                pic.user_profile_picture = media.user.profile_picture
                pic.picture_id = media.id
                pic.picture_url_low = media.images['low_resolution'].url
                pic.picture_url_high = media.images['standard_resolution'].url
                
                try:
                    pic.location_lat = media.location.point.latitude
                    pic.location_lng = media.location.point.longitude
                    pic.location_name = media.location.name
                except:
                    pass
                
                pic.save()
                pic.subscriptions.add(self)
                pic.save()

                #pic.find_related_pixel()
                                            
class Mosaic(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="mosaic/")
    tags = models.ManyToManyField(Tag)
    location_lat = models.FloatField(blank=True, null=True)
    location_lng = models.FloatField(blank=True, null=True)
    subscriptions = models.ManyToManyField(Subscription, related_name="mosaics")
    pixel_size = models.IntegerField()    
    is_parse = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):
        return self.name
    
    def pixel_count(self):
        return self.pixels.all().count()
    
    def pixel_associate_count(self):
        return self.pixels.filter(pic__isnull=False).count()
        
    def percent_complete(self):
        if self.pixels.all().count() > 0:
            print float(12) / float(3844) * float(100)
            return float(self.pixels.filter(pic__isnull=False).count()) / float(self.pixels.all().count()) * 100
        else:
            return 0
        
    #@transaction.commit_on_success
    def parse_pixesl(self):
        image = Image.open(self.image.path)
        pixels = list(image.getdata())
        width, height = image.size
        pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
        
        pixelSize = self.pixel_size
        middlePixel = pixelSize/2
        
        i=middlePixel
        coorX=0
        while i < width:
            
            if i<width:
                j=middlePixel
                coorY=0
                while j < height:
                    print j
                    print i
                    if j<height:
                        hexaColor = struct.pack('BBB',*pixels[i][j]).encode('hex')
                        if hexaColor != 'ffffff':
                            try:
                                pix = Pixel.objects.get(x=coorX,y=coorY,mosaic=self)
                                print "update pixel %s" % pix.id
                            except Pixel.DoesNotExist:
                                #self.stdout.write('Add pixel %s,%s' % (coorX, coorY))
                                print "add pixel"
                                pix = Pixel.objects.create(x=coorX,y=coorY,mosaic=self)

                            #self.stdout.write('Update pixel %s,%s with color : %s' % (coorX, coorY, hexaColor))
                            pix.color = hexaColor
                            pix.r_color = pixels[i][j][0]
                            pix.g_color = pixels[i][j][1]
                            pix.b_color = pixels[i][j][2]
                            pix.save()
                    j=j+pixelSize
                    coorY=coorY+pixelSize
            i=i+pixelSize
            coorX=coorX+pixelSize
        self.is_parse = True
        self.save()
                
    def save(self, size=(620, 620)):
        """
        Save Photo after ensuring it is not blank.  Resize as needed.
        """

        super(Mosaic, self).save()

        image = Image.open(self.image.path)  
        image = image.resize(size, Image.ANTIALIAS)  
        image.save(self.image.path) 
    
class InstaPic(models.Model):
    link = models.TextField()
    user_id = models.IntegerField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True, default='')
    user_profile_picture = models.TextField()
    picture_id = models.CharField(max_length=100, blank=True)
    picture_url_low = models.TextField()
    picture_url_high = models.TextField()
    color = models.CharField(max_length=6, blank=True, default='')
    r_color = models.IntegerField(max_length=3, blank=True, null=True)
    g_color = models.IntegerField(max_length=3, blank=True, null=True)
    b_color = models.IntegerField(max_length=3, blank=True, null=True)
    location_lat = models.FloatField(blank=True, null=True)
    location_lng = models.FloatField(blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True, default='')
    subscriptions = models.ManyToManyField(Subscription, related_name="instapics")
    is_parse = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)    
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def image_tag(self):
        return u'<img width=70px src="%s" />' % self.picture_url_low
    
    def color_block(self):
        return u'#%s : <div style="float:right; background-color:#%s; width:10px; height:10px;"></div>' % (self.color,self.color)
    
    def find_related_pixel(self):
        self.is_parse = True

        try:
            fileimage = cStringIO.StringIO(urllib.urlopen(self.picture_url_high).read())
            img = Image.open(fileimage)
            imgResze = img.resize((1, 1), Image.ANTIALIAS)
            pixels = list(imgResze.getdata())
        except:
            print 'error color pixel'
            self.delete()
            return True
        
        color_insta = RGBColor(pixels[0][0],pixels[0][1],pixels[0][2])
        color_hex = color_insta.get_rgb_hex()
        color_hex = color_hex.replace("#", "")
                
        self.color = color_hex
        self.r_color = pixels[0][0]
        self.g_color = pixels[0][1]
        self.b_color = pixels[0][2]
        
        pixel_asso = None    
        for subscription in self.subscriptions.all():
            print 'Subscription => %s' %  subscription
            for mosaic in subscription.mosaics.all():
                print 'Mosaic : %s' % mosaic.name
                try:
                    img = img.resize((mosaic.pixel_size, mosaic.pixel_size), Image.ANTIALIAS)
                    filepath = settings.MEDIA_ROOT + '/pics/%s_%s.jpg' % (mosaic.pixel_size,self.id)
                    img.save(filepath, 'JPEG')
                except:
                    print 'error save pixel min'
                    return True
                
                color_insta = RGBColor(pixels[0][0],pixels[0][1],pixels[0][2])
                color_hex = color_insta.get_rgb_hex()
                color_hex = color_hex.replace("#", "")
                delta_e = 100   
                 
                for pixel in mosaic.pixels.filter(pic__isnull=True):
                    pixel_color = RGBColor(pixel.r_color,pixel.g_color,pixel.b_color)
                    delta_e_new = color_insta.delta_e(pixel_color)
                    #print '#'+pixel.color 
                    #print color_insta.get_rgb_hex() 
                    #print delta_e_new 
                    if delta_e_new < delta_e:
                        delta_e = delta_e_new
                        pixel_asso = pixel
                print 'minimum delta_e %s' % delta_e
                if delta_e < 25:
                    print 'set pixel %s with delta %s' % (pixel_asso.id,delta_e)
                    pixel_asso.pic = self
                    pixel_asso.save()
                    self.add_to_fake_mosaic(mosaic, pixel_asso)
        self.save()
        
    def has_pixel(self):
        if self.pixels.count() >0:
            return True
        else:
            return False

    def add_to_fake_mosaic(self, mosaic, pixel):
        mosaic_path = settings.MEDIA_ROOT + '/mosaic/bg_%s.jpg' % mosaic.id

        img = Image.open(mosaic_path)

        filepath = settings.MEDIA_ROOT + '/pics/%s_%s.jpg' % (mosaic.pixel_size,pixel.pic.id)

        try:
            img.paste(Image.open(filepath), (pixel.y,pixel.x))
        except:
            #pixel.pic.delete()
            pass

        img.save(mosaic_path)
                
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    color_block.allow_tags = True
    
class Pixel(models.Model):
    color = models.CharField(max_length=6, blank=True, default='')
    r_color = models.IntegerField(max_length=3, blank=True, null=True)
    g_color = models.IntegerField(max_length=3, blank=True, null=True)
    b_color = models.IntegerField(max_length=3, blank=True, null=True)
    x = models.IntegerField(blank=True, default='')
    y = models.IntegerField(blank=True, default='')
    mosaic = models.ForeignKey(Mosaic, related_name="pixels",on_delete=models.CASCADE)
    pic = models.ForeignKey(InstaPic, blank=True, null=True, on_delete=models.SET_NULL, related_name="pixels")
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def color_block(self):
        return u'#%s : <div style="float:right; background-color:#%s; width:%spx; height:%spx;"></div>' % (self.color,self.color,self.mosaic.pixel_size,self.mosaic.pixel_size)
    
    def pic_color(self):
        if(self.pic):
            return u'#%s : <div style="float:right; background-color:#%s; width:%spx; height:%spx;"></div>' % (self.pic.color,self.pic.color,self.mosaic.pixel_size,self.mosaic.pixel_size)
        else:
            return u''
    
    color_block.allow_tags = True
    pic_color.allow_tags = True

@receiver(pre_delete, sender=Subscription, dispatch_uid='subscription_delete_signal')
def subscription_delete_signal(sender, instance, using, **kwargs):
    try:
        api.delete_subscriptions(id=instance.subscription_id)
    except:
        pass
