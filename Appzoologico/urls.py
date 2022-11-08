from django.urls import path

from Appzoologico.views import view_zool, form_add_animal

urlpatterns = [
    path('', view_zool),
    path('/form_add_animal', form_add_animal, name="add_animal"),
]