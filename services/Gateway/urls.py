from Gateway.views.med_records import medView
from Gateway.views.mhealth import MhealthView
from django.contrib import admin
from utils.views.login import Login
from utils.views.logout import Logout
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
#3333


admin.site.site_header = 'Gateway - Admin'


urlpatterns = [
    path('med-records/', medView.as_view()),
    path('mhealth/', MhealthView.as_view()),
    path('admin-gateway/', admin.site.urls),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
