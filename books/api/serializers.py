from rest_framework import serializers
from books.models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        # fields = '__all__'  # if we write this, book choice will be visible on comment
        exclude = ['book']


class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
