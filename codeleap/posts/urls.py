from django.urls import path
from posts.views.post import PostView

urlpatterns = [
    path('posts/', PostView.as_view(), name= "posts"),
    path('posts/<int:pk>', PostView.as_view(), name= "posts")
]