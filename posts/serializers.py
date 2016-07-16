from rest_framework import routers, serializers, viewsets, permissions

from .models import Post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
