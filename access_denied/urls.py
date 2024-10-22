from django.urls import path
from access_denied.views import AccessDeniedView

urlpatterns = [
    path('', AccessDeniedView.as_view(), name='access_denied'),
]                
                