from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    image = models.ImageField(upload_to="posts")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
