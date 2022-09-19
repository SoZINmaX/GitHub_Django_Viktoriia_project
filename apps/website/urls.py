from django.urls import path
from .views import CommentAPIView, ClientAPIView, ClientAPIDetailView, CommentAPIDetailView

app_name = 'apps.website'

urlpatterns = [
    path('api/v1/comment/list_add/', CommentAPIView.as_view(), name='comment_list_add'),
    path('api/v1/comment/delete_update/<int:pk>/', CommentAPIDetailView.as_view(), name='comment_delete_update'),
    path('api/v1/client/list_add/', ClientAPIView.as_view(), name='client_list_add'),
    path('api/v1/client/delete_update/<int:pk>/', ClientAPIDetailView.as_view(), name='comment_delete_update'),
]