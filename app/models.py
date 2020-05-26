from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Article(models.Model):
    titleEn = models.CharField(max_length=100, unique=True)
    titleAr = models.CharField(max_length=100, unique=True)
    titleEr = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    miniature = models.CharField(max_length=100)

    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    mins_read = models.IntegerField()

    def __str__(self):
        return self.titleEn


class Comment(models.Model):
    mComment = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class ArticleSession(models.Model):
    ip_address = models.CharField(max_length=50)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    finsh_date = models.DateTimeField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)


class Paragraph(models.Model):
    order = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    textEn = models.TextField()
    textFr = models.TextField()
    textAr = models.TextField()

    miniature = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    label = models.CharField(max_length=30, unique=True)
    color_code = models.TextField(max_length=20)

    def __str__(self):
        return self.label


class CategoryTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Page(models.Model):
    page_ref = models.IntegerField()


class Label(models.Model):
    labelEn = models.CharField(max_length=50)
    labelFr = models.CharField(max_length=50)
    labelAr = models.CharField(max_length=50)
    css_class = models.CharField(max_length=50)
    css_id = models.CharField(max_length=50)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
