from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings


# Create your models here.

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    
def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slug = slugify(instance.title)
        instance.slug = f'{slug}-{instance.id}'

pre_save.connect(article_pre_save, sender=Article)


# def article_post_save(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.slug = slugify(instance.title)
#         instance.save()

# post_save.connect(article_post_save, sender=Article)