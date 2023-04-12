from rest_framework import serializers
from .models import Post, Reply

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'create_time', 'update_time', 'reply_count', 'view_count', 'is_closed')

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'user', 'post', 'content', 'create_time', 'update_time', 'is_deleted')
