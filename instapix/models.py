import json

from datetime import datetime
from django.db import models
from instagram.client import InstagramAPI
from django.conf import settings
from django.core.exceptions import ValidationError

api = InstagramAPI(client_id=settings.INSTAGRAM_CONFIG['client_id'], client_secret=settings.INSTAGRAM_CONFIG['client_secret'])

USER_SUBSCRIPTION = 'user'
GEO_SUBSCRIPTION = 'user'
TAG_SUBSCRIPTION = 'user'
LOC_SUBSCRIPTION = 'user'
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
    tags = models.ManyToManyField(Tag,blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)    
    last_update = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def clean(self):
        if self.type == GEO_SUBSCRIPTION and (self.location_lat is None or self.location_lng is None or self.radius is None):
            raise ValidationError('For goegraphy subscription, lat, lng and radius required')
            
    def save(self, *args, **kwargs):
        update_sub = kwargs.pop('add_usbscription', True)
        if update_sub:
            if self.pk is not None:
                api.delete_subscriptions(id=self.subscription_id)
    
            if self.type == GEO_SUBSCRIPTION:
                res = api.create_subscription(object='geography', lat=self.location_lat, lng=self.location_lng, radius=self.radius, aspect='media', callback_url=settings.INSTAGRAM_CONFIG['redirect_uri'])
                self.subscription_id = res['data']['id']
                self.object_id = res['data']['object_id']
        else:
            self.last_update = datetime.now()
        
        return super(Subscription, self).save(*args, **kwargs)
    
    def delete(self):
        api.delete_subscriptions(id=self.subscription_id)
        super(Subscription, self).delete()
        
    def set_last_update(self):
        self.last_update = datetime.now()
        self.save(add_usbscription=False)
        
    def update_subscription(self):
        self.set_last_update()
        mosaics = self.mosaics
        if self.type == GEO_SUBSCRIPTION:
            recent_media, next = api.geography_recent_media(20, '', self.object_id)
            print recent_media
            for media in recent_media:
                if media.type =='image':
                    pic = InstaPic()
                    pic.link = media.link
                    pic.user_id = media.user.id
                    pic.user_name = media.user.username
                    pic.user_profile_picture = media.user.profile_picture
                    pic.picture_id = media.id
                    pic.picture_url_low = media.images.low_resolution.url
                    pic.picture_url_high = media.images.standard_resolution.url
                    #pic.color = 
                    if media.location is not None:
                        pic.location_lat = media.location.latitude
                        pic.location_lng = media.location.longitude
                        pic.location_name = media.location.name
                    pic.save()    
                    for mosaic in mosaics:
                        mosaic.add(pic)
                        mosaic.save()
                    
    def __unicode__(self):
        return u'%s' % self.subscription_id
    
class Mosaic(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="mosaic/")
    tags = models.ManyToManyField(Tag)
    location_lat = models.FloatField(blank=True)
    location_lng = models.FloatField(blank=True)
    subscriptions = models.ManyToManyField(Subscription, related_name="mosaics")
    is_parse = models.BooleanField()
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):
        return self.name
    
class InstaPic(models.Model):
    link = models.TextField()
    user_id = models.IntegerField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True, default='')
    user_profile_picture = models.TextField()
    picture_id = models.IntegerField(max_length=100, blank=True)
    picture_url_low = models.TextField()
    picture_url_high = models.TextField()
    color = models.CharField(max_length=6, blank=True, default='')
    location_lat = models.FloatField(blank=True)
    location_lng = models.FloatField(blank=True)
    location_name = models.CharField(max_length=255, blank=True, default='')
    publish_date = models.DateTimeField(auto_now_add=True)    
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def image_tag(self):
        return u'<img src="%s" />' % self.picture_url_low
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
class Pixel(models.Model):
    color = models.CharField(max_length=6, blank=True, default='')
    x = models.IntegerField(blank=True, default='')
    y = models.IntegerField(blank=True, default='')
    mosaic = models.ForeignKey(Mosaic, related_name="pixels")
    pic = models.ForeignKey(InstaPic, blank=True, null=True, related_name="pixels")
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def color_block(self):
        return u'#%s : <div style="float:right; background-color:#%s; width:10px; height:10px;"></div>' % (self.color,self.color)
    color_block.allow_tags = True

    
