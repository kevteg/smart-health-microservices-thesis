from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


decorators = [csrf_exempt]


@method_decorator(decorators, name='dispatch')
class Login(View):

    def dispatch(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user.groups)
        if user is not None:
            login(request, user)
            return JsonResponse({'In': True}, status=200)
        else:
            return JsonResponse({'In': False}, status=404)

