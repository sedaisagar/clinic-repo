from django.urls import path

from admin_panel.views.banners import BannerView
from admin_panel.views.common_views import AdminHomeView,AdminLoginView,AdminLogoutView



urlpatterns = [
    path("", AdminHomeView.as_view(), name="admin-index-page"),
    # AUTH VIEWS
    path("login/", AdminLoginView.as_view(), name="admin-login-page"),
    path("logout/", AdminLogoutView.as_view(), name="admin-logout-page"),

    # Home Page VIEWS

    path("banners/", BannerView.as_view(), name="admin-banner-page"),



]