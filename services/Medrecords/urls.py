from Medrecords.views.graphql import Graph
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from Gateway.views.login import Login
from Gateway.views.logout import Logout
from Medrecords.utils.helper import logged_user
from django.contrib.auth.decorators import user_passes_test

admin.site.site_header = 'Med records - Admin'


urlpatterns = [
    path('admin-med-records/', admin.site.urls),
    path('api/', user_passes_test(logged_user, login_url='/login/')(csrf_exempt(GraphQLView.as_view(graphiql=True)))),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
