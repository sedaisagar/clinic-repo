from django.urls import path

from public_panel.views import (
    PublicAboutView, 
    PublicHomeView,
    PublicServicesView,
    PublicDepartmentsView,
    PublicDepartmentDetailView,
    PublicDoctorsView,
    PublicDoctorDetailView,
    PublicAppointmentView,
    PublicBlogsView,
    PublicBlogDetailView,
    PublicContactView,
    DashboardLoginView,
    DashboardRegisterView,
    DashboardIndexView,
    DashboardLogoutView,
)

urlpatterns = [
    path("", PublicHomeView.as_view(), name="index-page"),
    path("about/", PublicAboutView.as_view(), name="about-page"),
    path("services/", PublicServicesView.as_view(), name="service-page"),
    path("departments/", PublicDepartmentsView.as_view(), name="department-page"),
    path("departments/<str:pk>", PublicDepartmentDetailView.as_view(), name="department-detail-page"),
    path("doctors/", PublicDoctorsView.as_view(), name="doctor-page"),
    path("doctors/<str:pk>", PublicDoctorDetailView.as_view(), name="doctor-detal-page"),
    path("appointment/", PublicAppointmentView.as_view(), name="appointment-page"),
    path("blogs/", PublicBlogsView.as_view(), name="blog-page"),
    path("blogs/<str:pk>", PublicBlogDetailView.as_view(), name="blog-detail-page"),
    path("contact/", PublicContactView.as_view(), name="contact-page"),
    
    # Dashboard URLs
    path("dashboard/", DashboardIndexView.as_view(), name="dashboard-index"),
    path("dashboard/login/", DashboardLoginView.as_view(), name="dashboard-login"),
    path("dashboard/register/", DashboardRegisterView.as_view(), name="dashboard-register"),
    path("dashboard/logout/", DashboardLogoutView.as_view(), name="dashboard-logout"),
]