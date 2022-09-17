from django.urls import path
from .views import CommentAPIView

app_name = 'apps.website'

urlpatterns = [
    path('api/v1/comment_list', CommentAPIView.as_view(), name='comment_list'),
]