from django.urls import path, include

from .views import LabourListApiView, LabourDetailApiView

app_name = "labours"

urlpatterns = [
    path("labours/", LabourListApiView.as_view(), name="list"),
    path("labours/<int:pk>", LabourDetailApiView.as_view(), name="detail"),

]
