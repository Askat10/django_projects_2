from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET'])
def get_books(request: Request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)