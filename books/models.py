from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    preface = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField()

    def __str__(self):
        return f'{self.author} - {self.name}'


class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='comments')
    # comment_owner = models.CharField(max_length=255)
    comment_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.rating)
