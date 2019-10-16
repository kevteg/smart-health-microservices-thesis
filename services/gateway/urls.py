from gateway.views.med_records import medView
from django.urls import path
from django.conf.urls import url, include
#3333

urlpatterns = [
    path('med-records/', medView.as_view())
]
