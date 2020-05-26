from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
import json

from .serializers import *


class PostApiView(APIView):

    def post(self, request, slug):

        slug = self.kwargs.get('slug')
        data = get_object_or_404(Article, slug=slug)
        serializer = ArticleSerializer([data], many=True)

        return Response(serializer.data)


class ArticleTagApiView(APIView):

    def post(self, request, slug):

        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article, slug=slug)
        foo = ArticleTag.objects.filter(article_id=article.id)
        data = []
        for m in foo:
            tag = Tag.objects.get(pk=m.tag.id)

            data.append(
                {
                    'label': tag.label,
                    'color_code': tag.color_code,
                }
            )
        serializer = TagSerializer(data, many=True)

        return Response(serializer.data)


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""     def get_queryset(self):
            return Category.objects.filter() """


class PostListApiView(APIView):

    def post(self, request):
        #serializer = SnippetSerializer(data=request.data)
        data = Article.objects.order_by('-mins_read')
        foo = request.data["tags"]
        tags_id = []
        for f in foo:
            tag_id = f['id']
            tags_id.append(tag_id)

        #################

        serializer = ArticleSerializer(data, many=True)
        return Response(serializer.data)


class GetTagsApiView(APIView):
    def post(self, request, slug):

        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article, slug=slug)
        foo = ArticleTag.objects.filter(article_id=article.id)[:4]
        data = []
        for m in foo:
            tag = Tag.objects.get(pk=m.tag.id)

            data.append(
                {
                    'label': tag.label,
                    'color_code': tag.color_code,
                }
            )
        serializer = TagSerializer(data, many=True)
        return Response(serializer.data)
