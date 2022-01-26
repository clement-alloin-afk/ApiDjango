from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FamilyDetail, UserList,UserDetail, FamilyList
from . import views

urlpatterns = [
    path('User/', UserList.as_view()),
    path('User/<pk>', UserDetail.as_view()),
    path('Family/', FamilyList.as_view()),
    path('Family/<int:pk>/', FamilyDetail.as_view()),
    re_path(r'^family/(?P<code>[A-Z0-9]{10})/$', views.FamilyCode),
]

urlpatterns = format_suffix_patterns(urlpatterns)