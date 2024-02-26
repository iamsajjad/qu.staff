
from django.urls import path
from search.views import search, getstaff

urlpatterns = (
    path('', search, name='search'),
    path('getstaff/', getstaff, name='getstaff'),
)

