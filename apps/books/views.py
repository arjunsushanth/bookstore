from django.shortcuts import render
import cloudinary.uploader
from rest_framework import status, generics, filters
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer, BookAddSerializer
from apps.users.authentications import CustomAuthentication
import re
# Create your views here.

class BookList(generics.ListAPIView):
    # authentication_classes = [CustomAuthentication]
    queryset = Book.objects.order_by('-created_at')
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'author__pseudonym', 'author__first_name', 'author__last_name']


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAdd(APIView):
    authentication_classes = [CustomAuthentication]
    
    def post(self, request, *args, **kwargs):
        pseudonym = re.sub('[^A-Za-z]+', '', request.user.pseudonym) #remove all special char and alpha numeric
        username = re.sub('[^A-Za-z]+', '', request.user.username)
        if pseudonym.lower()=='darthvader' or username.lower()=='darthvader': #check user is darth vader
            return Response({'error': 'You cannot publish books'})
        request.data['author'] = request.user.id
        serializer = BookAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdate(generics.UpdateAPIView):
    authentication_classes = [CustomAuthentication]
    
    def update(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=self.kwargs['pk'], author_id=request.user.id) #get the particular book of the user
            cover_image = request.FILES.get('cover_image', None)
            if "cover_image" is not None: #if new cover image is uploaded then delete the old image from cloud
                cloudinary.uploader.destroy(book.cover_image.public_id, invalidate=True) 
            serializer = BookAddSerializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({'error': 'not owned'}, 
                                status=status.HTTP_404_NOT_FOUND)




