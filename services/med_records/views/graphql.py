import logging
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

decorators = [csrf_exempt]


@method_decorator(decorators, name='dispatch')
class Graph(View):
    
    method = 'GET'

    def dispatch(self, request, *args, **kwargs):
        data = {'med-records': '1'}
        response = JsonResponse(data, status=200)
        response["Access-Control-Allow-Origin"] = '*'
        return response

