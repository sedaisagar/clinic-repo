from django.urls import path

from admin_panel.views import AdminHomeView,AdminLoginView,AdminLogoutView


urlpatterns = [
    path("login/", AdminLoginView.as_view(), name="admin-login-page"),
    path("logout/", AdminLogoutView.as_view(), name="admin-logout-page"),
    path("", AdminHomeView.as_view(), name="admin-index-page")
]