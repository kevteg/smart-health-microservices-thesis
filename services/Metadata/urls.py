from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from utils.views.login import Login
from utils.views.logout import Logout
from utils.helper import logged_user
from django.contrib.auth.decorators import user_passes_test

admin.site.site_header = 'Metadata - Admin'


urlpatterns = [
    path('admin-metadata/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
