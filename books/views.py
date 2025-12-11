from rest_framework import viewsets
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

def index(request):
    return render(request, 'books/index.html')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer