import os
from django.conf.urls import url, include
from django.urls import path
APP = os.environ['APP']

urlpatterns = [
    path('',  include(f'{APP}.urls'))
]
