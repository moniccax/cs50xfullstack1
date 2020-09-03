from django.urls import path

from . import views
from . import util

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path('create/', views.create, name="create"),
    path('monica/', views.monica, name='monica'),
    path('random/', views.random, name='random')

]


#verificar random depois com dani
