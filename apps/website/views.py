from rest_framework import generics
from .models import Comment, Client
from .serializers import CommentSerializer, ClientSerialier
from rest_framework.permissions import IsAdminUser


class CommentAPIView(generics.ListCreateAPIView): 
    queryset = Comment.objects.order_by('-rate', '-date')
    serializer_class = CommentSerializer
    
   
class CommentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUser, )
    
    
class ClientListAPIView(generics.ListAPIView): 
    queryset = Client.objects.all()
    serializer_class = ClientSerialier
    permission_classes = (IsAdminUser, )
    
class ClientCreateAPIView(generics.CreateAPIView): 
    queryset = Client.objects.all()
    serializer_class = ClientSerialier
    throttle_scope = 'create_client'
    

class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier
    permission_classes = (IsAdminUser, )