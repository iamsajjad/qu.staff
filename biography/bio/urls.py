
from django.urls import path
from bio.views import mainpage, biopage, edit

urlpatterns = (
    path('', mainpage, name='mainpage'),
    path('edit/<str:slug>', edit, name='edit'),
    path('<str:slug>', biopage, name='biopage'),
)

