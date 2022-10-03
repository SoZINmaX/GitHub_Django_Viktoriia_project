from rest_framework import generics
from .models import Comment, Client
from .serializers import CommentSerializer, ClientSerialier
from .permissions import IsAdminReadOnly


class CommentAPIView(generics.ListCreateAPIView): 
    queryset = Comment.objects.order_by('-rate', '-date')
    serializer_class = CommentSerializer
    
   
class CommentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminReadOnly, )
    
    
class ClientAPIView(generics.ListCreateAPIView): 
    queryset = Client.objects.all()
    serializer_class = ClientSerialier
    

class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier
    permission_classes = (IsAdminReadOnly, )