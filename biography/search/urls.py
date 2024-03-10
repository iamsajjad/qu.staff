
from django.urls import path
from search.views import search, getstaff, excel

urlpatterns = (
    path('', search, name='search'),
    path('getstaff/', getstaff, name='getstaff'),
    path('excel/', excel, name='excel'),
)

