import os
from django.conf.urls import url, include
from django.urls import path
DJANGO_CONFIGURATION = os.environ['DJANGO_CONFIGURATION']

urlpatterns = [
    path('',  include(f'{DJANGO_CONFIGURATION}.urls'))
]
