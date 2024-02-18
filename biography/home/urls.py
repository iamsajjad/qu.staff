
from django.urls import path
from home.views import homepage, language, notfound

urlpatterns = (
    path('', homepage, name='homepage'),
    path('language/<path:pagepath>', language, name='language'),
    path('notfound/', notfound, name='notfound'),
)

