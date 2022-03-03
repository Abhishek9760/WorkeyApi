from django.urls import path

from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token


from .views import AuthAPIView, RegisterAPIView

app_name = "auth"

urlpatterns = [
    path("login/", AuthAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("verify/", verify_jwt_token),
    path("obtain/", obtain_jwt_token)
]
