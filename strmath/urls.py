
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from calcu.views import index
from users.views import login_view, login_signup, logout_view, signup_view, user_panel, update_personal_info, update_password

# 3. add views from simple jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='home'),

    path('authuser/',login_signup , name='auth'),
    path('authuser/login/',login_view , name='login'),
    path('logout/', logout_view, name='logout'),

    path('authuser/signup/', signup_view, name='signup'),

    path("update/", update_personal_info, name='update'),

    path('userpanel/', user_panel, name='userpanel'),

    path('update_password/', update_password, name='updatepass'),


    # Forget Password
    # صفحه درخواست بازنشانی رمز عبور
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    # صفحه‌ای که می‌گوید ایمیل بازیابی ارسال شد
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    # صفحه‌ای که کاربر از طریق لینک ایمیل به آن هدایت می‌شود
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),

    # صفحه‌ای که پس از تغییر موفقیت‌آمیز رمز عبور نمایش داده می‌شود
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),

    # 4. add path from simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
