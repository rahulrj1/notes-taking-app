from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun1, name="path1"),
    path('delete/<str:pk>/',views.fun2, name="deletetask"),
    path('update/<str:pk>/',views.fun3, name="updatetask"),
]
