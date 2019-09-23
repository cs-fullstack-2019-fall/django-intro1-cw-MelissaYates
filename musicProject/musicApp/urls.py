from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('music/',views.music),
    path('music/barbra/',views.barbra),
    path('music/michael/',views.michael),
    path('music/vanessa/',views.vanessa),
]