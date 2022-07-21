from django.urls import path
from .views import wordCount, countDelete

urlpatterns = [
    path('', wordCount),
    path('', countDelete, name = 'file_delete')
]
