import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.views.generic.base import View
from django.shortcuts import render
from instapix.models import Mosaic, Subscription
from django.http import HttpResponse
from instagram.client import InstagramAPI
from django.conf import settings

api = InstagramAPI(client_id=settings.INSTAGRAM_CONFIG['client_id'], client_secret=settings.INSTAGRAM_CONFIG['client_secret'])

class MosaicPreview(View):
    """
    View to list all pictures in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    template_name = 'mosaic_detail.html'

    def get(self, request, mosaic_id, *args, **kwargs):
        mosaic = Mosaic.objects.get(id=mosaic_id);

        return render(request, self.template_name, {'mosaic':mosaic})
        

class MosaicRealtime(View):
    """
    View to list all pictures in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    template_name = 'mosaic_detail.html'

    def get(self, request, *args, **kwargs):
        challenge =  request.GET.get('hub.challenge')
        return HttpResponse(challenge, content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        for object in json_data:
            subscription_id = object['subscription_id']
            try:
                subscription = Subscription.objects.get(subscription_id=subscription_id)
                subscription.update_subscription()
            except Subscription.DoesNotExist:
                pass
                
        return HttpResponse("ok")
