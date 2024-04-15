import graphene
from graphene_django import DjangoObjectType
from .models import Comment

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("email", "body", "name", "date_added")

class Query(graphene.ObjectType):
    all_Comment = graphene.List(CommentType)

schema = graphene.Schema(query=Query)