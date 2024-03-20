
from django.urls import path
from search.views import search, group, excel

urlpatterns = (
    path('', search, name='search'),
    path('group', group, name='group'),
    path('excel/', excel, name='excel'),
)

