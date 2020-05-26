
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('get_post/<slug>',
         PostApiView.as_view(), name="api_get_post"),
    path('get_categories', CategoryApiView.as_view(),
         name="api_get_categories"),
    path('get_article_tags/<slug>', ArticleTagApiView.as_view(),
         name="api_get_article_categories"),
    path('get_posts/', PostListApiView.as_view(),
         name="api_get_posts"),
    path('get_tags/<slug>', GetTagsApiView.as_view(),
         name="api_get_tag"),

]
