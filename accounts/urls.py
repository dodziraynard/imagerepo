from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.my_images, name="my_images"),
    path('upload', login_required(views.UploadImage.as_view(),
                                  login_url="accounts:login"), name="upload_image"),

    path('operate-images', views.operate_images, name="operate_images"),

    path('login', views.UserLogin.as_view(), name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.UserRegistration.as_view(), name="register"),
]
