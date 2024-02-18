
from django.urls import path
from link.views import new, edit, delete

urlpatterns = (
    path('link/new/<str:slug>', new, name='new_link'),
    path('link/edit/<str:slug>/<int:linkid>', edit, name='edit_link'),
    path('link/delete/<str:slug>/<int:linkid>', delete, name='delete_link'),
)

