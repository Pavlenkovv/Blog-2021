from django.db import models
from uuid import uuid4
from os import path


class Post(models.Model):
    def get_file_name_posts(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/posts/', filename)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_name_posts, null=True)
    comment_to_post = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Title: {self.title}'


class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False)
    post_being_commented = models.ForeignKey(Post, on_delete=models.CASCADE, null=False,
                                             blank=False)
    body = models.TextField(max_length=1000, null=False, blank=False)


    def __str__(self):
        return f'Comment to the: {self.post_being_commented} | {self.body}'
