from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __unicode__(self):
        return self.name
    
class Mosaic(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="mosaic/")
    tags = models.ManyToManyField(Tag)
    location_lat = models.FloatField(blank=True)
    location_lng = models.FloatField(blank=True)
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
    user_profile_picture = models.TextField()
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

    
