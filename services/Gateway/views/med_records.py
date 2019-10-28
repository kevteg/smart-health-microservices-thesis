from django.views.generic import View
import json
import logging
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import UserPassesTestMixin


decorators = [csrf_exempt]


@method_decorator(decorators, name='dispatch')
class medView(View):

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user and user.is_superuser:
            data = arguments = json.loads(request.body)
            response = JsonResponse(data, status=200)
            response["Access-Control-Allow-Origin"] = '*'
        else:
            response = JsonResponse({'authentication-error': True}, status=503)
        return response

