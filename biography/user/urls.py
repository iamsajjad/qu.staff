
from django.urls import path
from user.views import reset, signin, register, signout

urlpatterns = (
    path('password/reset', reset, name="reset"),
    path('', signin, name="signin"),
    path('signin', signin, name="signin"),
    path('register', register, name="register"),
    path('signout', signout, name='signout'),
)

