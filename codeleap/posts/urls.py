from django.urls import path
from posts.views.career import CareerView

urlpatterns = [
    path('career/', CareerView.as_view(), name= "career"),
    path('career/<int:pk>', CareerView.as_view(), name= "career")
]