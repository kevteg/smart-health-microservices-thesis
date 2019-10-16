
import logging
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


decorators = [csrf_exempt]


@method_decorator(decorators, name='dispatch')
class medView(View):

    def dispatch(self, request, *args, **kwargs):
        data = {'med-records': '1'}
        response = JsonResponse(data, status=200)
        response["Access-Control-Allow-Origin"] = '*'
        return response

