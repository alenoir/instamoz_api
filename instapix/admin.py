from django.contrib import admin
from instapix.models import Tag, Mosaic, Pixel, InstaPic, Subscription

class MosaicAdmin(admin.ModelAdmin):
    list_display = ('name', 'pixel_count', 'pixel_associate_count', 'percent_complete')
    search_fields = ['id']
    
class PixelAdmin(admin.ModelAdmin):
    list_display = ('id', 'mosaic', 'x', 'y', 'color_block', 'pic_color')
    search_fields = ['id']

class InstaPicAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'color_block', 'location_name', 'has_pixel', 'publish_date', 'create_date')
    
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_id', 'type', 'last_update', 'tag', 'location_lat', 'location_lng')

admin.site.register(Tag)
admin.site.register(Mosaic, MosaicAdmin)
admin.site.register(Pixel, PixelAdmin)
admin.site.register(InstaPic, InstaPicAdmin)
admin.site.register(Subscription, SubscriptionAdmin)