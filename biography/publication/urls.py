
from django.urls import path

from publication.views import new, edit, delete

urlpatterns = (
    path('publication/new/<str:slug>', new, name='new_publication'),
    path('publication/edit/<str:slug>/<int:pubid>', edit, name='edit_publication'),
    path('publication/delete/<str:slug>/<int:pubid>', delete, name='delete_publication'),
)

