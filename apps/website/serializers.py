from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Comment, Client
from .tasks import send_comment_info_to_telegram, send_client_info_to_telegram

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"
    
    def create(self, validated_data):
        
        send_comment_info_to_telegram.delay(validated_data)
        
        return super().create(validated_data)
        
class ClientSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"
        
    def create(self, validated_data):
        
        send_client_info_to_telegram.delay(validated_data)
        
        return super().create(validated_data)