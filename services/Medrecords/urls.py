from Medrecords.views.graphql import Graph
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


admin.site.site_header = 'Med records - Admin'


urlpatterns = [
    path('admin-med-records/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
