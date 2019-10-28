from django.views.generic import View
from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


decorators = [csrf_exempt]


@method_decorator(decorators, name='dispatch')
class Logout(View):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({'out': True}, status=200)
