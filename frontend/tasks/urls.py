from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("update/<str:id>/", views.update_task, name="update_task"),
    path("delete/<str:id>/", views.delete_task, name="delete_task"),
]