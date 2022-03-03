from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.api.user.serializers import UserDetailSerializer
from labours.models import Labour

# from diary.api.serializers import DiaryInlineUserSerializer

User = get_user_model()


class LabourSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # diary = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserDetailSerializer()

    class Meta:
        model = Labour
        fields = "__all__"

    # def get_labour_info(self, obj):
    #     print(obj)
    #     return UserDetailSerializer(obj)

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse(
            "api-labour:detail", kwargs={"pk": obj.pk}, request=request
        )

    # def get_diary(self, obj):
    #     request = self.context.get("request")
    #     limit = 10
    #     if request:
    #         limit_query = request.GET.get("limit")
    #         try:
    #             limit = int(limit_query)
    #         except:
    #             pass
    #     qs = obj.diary_set.all().order_by("-timestamp")

    #     data = {
    #         "uri": self.get_uri(obj) + "diary/",
    #         "last": DiaryInlineUserSerializer(
    #             qs.first(), context={"request": request}
    #         ).data,
    #         "recent": DiaryInlineUserSerializer(
    #             qs[:limit], many=True, context={"request": request}
    #         ).data,
    #     }
    #     return data
