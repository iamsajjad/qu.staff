
from django.urls import path
from history.views import history

urlpatterns = (
    path('', history, name='history'),
)

