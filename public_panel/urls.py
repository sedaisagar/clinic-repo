from django.urls import path

from public_panel.views import PublicAboutView, PublicHomeView

urlpatterns = [
    path("", PublicHomeView.as_view(), name="index-page"),
    path("about/", PublicAboutView.as_view(), name="about-page"),
]