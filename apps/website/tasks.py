from celery import shared_task
import requests
from decouple import config     

TOKEN = config('TOKEN')
CHAT_ID = config('CHAT_ID')

       
@shared_task   
def send_comment_info_to_telegram(validated_data):
        
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
        
@shared_task   
def send_client_info_to_telegram(validated_data):
        
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
