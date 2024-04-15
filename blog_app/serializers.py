# serializers.py

from rest_framework import serializers
from .models import CreateBlog, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['email', 'body', 'name', 'date_added']

class CreateBlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = CreateBlog
        fields = ['title', 'slug', 'intro', 'body', 'image', 'date_added', 'comments']
