from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Comment, Client
import requests
from decouple import config
TOKEN = config('TOKEN')
CHAT_ID = config('CHAT_ID')

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"
    
    def create(self, validated_data):
        
        global TOKEN
        global CHAT_ID
        MESSAGE = f"\n \
        Hi Viktoriia 😇\n \
        \n \
        You have one new comment 🥳\n \
        \n \
        Name: {validated_data.get('name')}\n \
        Comment: {validated_data.get('comment')}\n \
        Rating: {validated_data.get('rate')}"
                            
        URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
        
        requests.get(URL)
        
        return super().create(validated_data)
        
class ClientSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"
        
    def create(self, validated_data):
        
        global TOKEN
        global CHAT_ID
        MESSAGE = f"\n \
        Hi Viktoriia 😇\n \
        \n \
        You have one client waiting for your response 🥳\n \
        \n \
        Name: {validated_data.get('name')}\n \
        Phone number: {validated_data.get('phone_number')}\n \
        Email: {validated_data.get('email')}\n \
        Message: {validated_data.get('message')}"
                            
        URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
        
        requests.get(URL)
        
        return super().create(validated_data)