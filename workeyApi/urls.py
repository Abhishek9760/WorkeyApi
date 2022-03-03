from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("accounts.api.urls", namespace="api-auth")),
    path("api/", include("labours.api.urls", namespace="api-labour")),

]
