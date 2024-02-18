
from django.urls import path
from settings.views import settings, password

urlpatterns = (
    path('', settings , name='settings'),
    path('password/', password, name='password'),
)

