from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Comment, Client


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class ClientSerialier(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"