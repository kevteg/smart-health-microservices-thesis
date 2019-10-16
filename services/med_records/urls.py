from med_records.views.graphql import Graph
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('graph/', Graph.as_view())
]
