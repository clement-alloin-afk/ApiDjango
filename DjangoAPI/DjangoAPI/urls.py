from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
