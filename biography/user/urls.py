
from django.urls import path
from user.views import signin, register, signout

urlpatterns = (
    path('', signin, name="signin"),
    path('signin/', signin, name="signin"),
    path('register/', register, name="register"),
    path('signout/', signout, name='signout'),
)

