from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer