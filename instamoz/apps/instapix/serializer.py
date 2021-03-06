from rest_framework import serializers

from instamoz.apps.instapix.models import Mosaic, Tag, Pixel, InstaPic


class InstaPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaPic
        fields = ('id', 'user_name', 'picture_url_high')

class PixelSerializer(serializers.ModelSerializer):
    pic = InstaPicSerializer()
    class Meta:
        model = Pixel
        fields = ('id', 'x', 'y', 'pic', 'color')
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        
class MosaicSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    fake_image = serializers.Field(source='fake_image')
    class Meta:
        model = Mosaic
        fields = ('id', 'name', 'tags', 'location_lat', 'location_lng', 'fake_image', 'pixel_size')