from rest_framework import serializers
from .models import UsersPosts

class UsersPostsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username") 

    class Meta:
        model = UsersPosts
        fields = [ "author", "title", "main_text", "publish_date"]
