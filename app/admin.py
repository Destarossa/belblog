from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(CategoryTag)
admin.site.register(ArticleTag)
