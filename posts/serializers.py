from rest_framework import routers, serializers, viewsets, permissions

from .models import Post


class BlogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='posts:detail_api')

    class Meta:
        model = Post

        fields = [
            'url',
            'user',
            'title',
            'image',
            'content',
            'timestamp',
        ]
