from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

# Time
class TimeStampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Article
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Article(TimeStampModel):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article_author')
    title = models.CharField(max_length=512)
    contents = RichTextField(null=True, blank=True)
    category = models.CharField(max_length=255, default='None')

    # likes = models.DecimalField()
    # dislikes = models.DecimalField()
    def get_absolute_url(self):
        return reverse('index')
        # must be fixed
        # return reverse('detail', args=(str(self.id)))


#
class Comment(TimeStampModel):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comment_author')
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL, related_name='article_comment')
    contents = models.TextField(blank=True)
