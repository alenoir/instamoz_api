from django.contrib import admin
from instapix.models import Tag, Mosaic, Pixel, InstaPic, Subscription

class PixelAdmin(admin.ModelAdmin):
    list_display = ('mosaic', 'x', 'y', 'color_block', 'pic')

admin.site.register(Tag)
admin.site.register(Mosaic)
admin.site.register(Pixel, PixelAdmin)
admin.site.register(InstaPic)
admin.site.register(Subscription)