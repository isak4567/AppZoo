from django.urls import path

from Appzoologico.views import view_zool, view_posts, view_about, view_contact

urlpatterns = [
    path('', view_zool, name="Home"),
    path('Posts/', view_posts, name="posts"),
    path('About/', view_about, name="about"),
    path('Contact/', view_contact, name="contact"),
]