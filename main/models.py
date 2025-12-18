from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
STATUS=[
    ("Draft","Draft"),
    ("Published","Published")
]

class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="draft")
class PublishedManager(models.Manager):
    def get_queryset(self)
        return super().get_queryset().filter(status="publised")

class PostModel(models.Model):
   
    title = models.CharField(max_length=250)#title
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish') #A short form of the inherited title but space is replaced with hyphen(-) and unique with date
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='draft')
    objects = models.Manager()      # default manager
    published = PublishedManager()  # custom manager for published posts
    drafts = DraftManager()
    class Meta:
        ordering = ('-publish',)

