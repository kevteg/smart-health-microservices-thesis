from django.views.generic import View
import json
import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


decorators = [csrf_exempt]
MHEALTH_URL = settings.MHEALTH_URL 


@method_decorator(decorators, name='dispatch')
class MhealthView(View):

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user and user.is_superuser:
            data = json.loads(request.body)
            response = requests.post(f'{MHEALTH_URL}/api/', json=data)
            response = JsonResponse(response.json(), status=200)
        else:
            response = JsonResponse({'authentication-error': True}, status=503)
        return response

