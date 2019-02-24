from django.urls import path
from . import views


app_name = "getapi"

urlpatterns = [
    path('', views.index, name="index"),
    path('response/', views.detail, name="detail")
]
