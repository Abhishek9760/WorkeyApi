from django.contrib.auth import get_user_model

from rest_framework import permissions, generics, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin

from labours.models import Labour

# from accounts.api.permissions import IsSelfUserOrAdminUserOrNotAllowed

from .serializers import LabourSerializer

# from diary.models import Diary
# from diary.api.serializers import DiaryInlineUserSerializer

User = get_user_model()


class LabourListApiView(generics.ListAPIView):
    serializer_class = LabourSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Labour.objects.filter(user___labour=True)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class LabourDetailApiView(generics.RetrieveAPIView):
    serializer_class = LabourSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        return Labour.objects.filter(pk=pk, user___labour=True)

    def get_serializer_context(self):
        return {"request": self.request}


# class UserDiaryAPIView(generics.ListAPIView):
#     serializer_class = DiaryInlineUserSerializer
#     # permission_classes = [IsSelfUserOrAdminUserOrNotAllowed, ]
#     ordering_fields = ['timestamp']
#     search_fields = ['title', 'text', ]

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get("username")
#         if not username:
#             return Diary.objects.none()
#         return Diary.objects.filter(user__username=username)


# class UserExistsAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request, *args, **kwargs):
#         username = kwargs.get('username')
#         email = request.GET.get('email')
#         errors = {"username": "", "email": ""}
#         if email:
#             email_obj = User.objects.filter(email__exact=email)
#             if email_obj.exists():
#                 errors['email'] = "Already exists"
#         if username:
#             user_obj = User.objects.filter(username__exact=username)
#             if user_obj.exists():
#                 errors["username"] = "Already taken"
#         return Response(errors, status=200)
