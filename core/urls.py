"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from account.views import UpdatePasswordView, UpdateProfileView
from core import settings
from signup.views import SignUpView

urlpatterns = [
                  path('mktcode/admin/', admin.site.urls),

                  # Accounts
                  path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
                  path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('password_change/', PasswordChangeView.as_view(), name='password_change'),
                  path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
                  path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
                  path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
                  path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
                  path('access_denied/', include('access_denied.urls')),
                  path('account/password/', UpdatePasswordView, name='update_password'),
                  path('account/profile/', UpdateProfileView, name='update_profile'),
                  path('signup/', SignUpView.as_view(), name='signup'),
                  path('home/', include('home.urls')),
                  path('message/private/', include('message_private.urls')),
                  path("app_instrument/", include('app_instrument.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Header Admin
admin.site.index_title = "Administração do Sistema"
