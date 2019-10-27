from Medrecords.views.graphql import Graph
from django.urls import path
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('graph/', Graph.as_view()),
    path('graphiql/', GraphQLView.as_view(graphiql=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
