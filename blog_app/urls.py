from django.urls import path
from blog_app.views import BlogListAPIView, BlogDetailView
from graphene_django.views import GraphQLView
from blog_app.schema import schema

app_name = 'blog_app'

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name="blog"),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
