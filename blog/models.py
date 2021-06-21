from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, blank=False, unique=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-date_added']

def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return
        
    instance.slug= slugify(instance.date_added)

pre_save.connect(set_slug, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


