from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('world', views.world, name="world"),
    path('business', views.busin, name="business"),
    path('sports', views.sports, name="sports"),
    path('science', views.science, name="science"),
    path('entertainment', views.ente, name="entertainment"),
]