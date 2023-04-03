from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/add/', views.BookAdd.as_view(), name='book_add'),
    path('books/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),


]