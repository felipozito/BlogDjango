from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
