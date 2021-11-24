from django.urls import path
from rest_framework import views
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/',
         api_views.BookDetailAPIView.as_view(), name='book-information'),
    path('books/<int:book_pk>/write_comment/',
         api_views.CommentCreateAPIView.as_view(), name='write-comment'),
    path('comments/<int:pk>',
         api_views.CommentDetailAPIView.as_view(), name='comments'),
]
