from django.db import models
from posts.models import Post


class Tag(models.Model):
    title = models.CharField(max_length=255)
    post = models.ManyToManyField(Post, related_name="tags")

    def __str__(self):
        return self.title


