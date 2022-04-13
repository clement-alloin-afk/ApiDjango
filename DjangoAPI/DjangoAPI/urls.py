from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TFE API",
      default_version='v1',
   ),
   public=True,
)
urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
