from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from blog_app.forms import BlogForm
from .models import CreateBlog
from .serializers import CreateBlogSerializer, CommentSerializer

class BlogListAPIView(APIView):
    def get(self, request):
        blogs = CreateBlog.objects.all()
        serializer = CreateBlogSerializer(blogs, many=True)
        context = {'blogs': serializer.data}
        return render(request, 'blog/blog.html', context)

from django.shortcuts import render

class BlogDetailView(APIView):
    def get(self, request, slug):
        post = CreateBlog.objects.get(slug=slug)
        comments = post.comments.all()
        context = {
            'article': post,
            'comments': comments,
            'form': BlogForm() 
        }
        return render(request, 'blog/update.html', context)


    def put(self, request, slug):
        blog = CreateBlog.objects.get(slug=slug)
        serializer = CreateBlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, slug):
        blog = self.get_object(slug)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
