from django.urls import path

from admin_panel.views import AdminHomeView

urlpatterns = [
    path("", AdminHomeView.as_view(), name="admin-index-page")
]