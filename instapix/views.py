from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.views.generic.base import View
from django.shortcuts import render
from instapix.models import Mosaic

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
        