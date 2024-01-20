from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('invoices.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line
]
