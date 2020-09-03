from django.urls import path, include

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    #path("create", views.create, name="create"),
    #path('create/', views.create, name="create"),
    path('create/', views.create, name="create"),
    path('monica', views.monica, name='monica'),
    path('<str:name>', views.greet, name='greet')

    #path('random/', views.random, name="random")
    #path('{your_name}/', views.entries)

]
