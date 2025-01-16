from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
       title = "API Documentation",
       default_version = 'v1',
       description = "Документация для вашего API",
       terms_of_service="https://www.yourapp.com/terms/",
       contact=openapi.Contact(email="contact@yourapp.com"),
       license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=True)),
    path('admin/', admin.site.urls),
    path('lms/', include('lms.urls')),
    path('api/users/', include('users.urls')),
    path('api/payments/', include('payments.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]