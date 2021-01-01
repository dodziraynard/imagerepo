from django.urls import path
from . import views

app_name = "web"
urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('images/<int:id>', views.image_details, name="image_details"),
]
