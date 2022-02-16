from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers


urlpatterns = [
    path(
        "token/obtain/", jwt_views.TokenObtainPairView.as_view(), name="token_create"
    ),  # override sjwt stock token
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
