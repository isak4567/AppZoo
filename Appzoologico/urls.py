from django.urls import path

from Appzoologico.views import view_zool

urlpatterns = [
    path('', view_zool),
]