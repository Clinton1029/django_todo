from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("delete/<int:id>/", views.delete_task, name="delete"),
]
