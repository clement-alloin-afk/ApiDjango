from django.urls import path
from .views import UserList, FamilyList, FamilyDetail

urlpatterns = [
    path('User/', UserList.as_view()),
    path('family/', FamilyList.as_view()),
    path('family/<int:pk>/', FamilyDetail.as_view()),
]