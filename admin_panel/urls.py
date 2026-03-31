from django.urls import path

from admin_panel.views.banners import BannerView
from admin_panel.views.common_views import AdminHomeView,AdminLoginView,AdminLogoutView
from admin_panel.views.testimonials import TestimonialCreateView, TestimonialDeleteView, TestimonialListView, TestimonialUpdateView
from admin_panel.views.trusted_partners import TrustedPartnersCreateView, TrustedPartnersDeleteView, TrustedPartnersListView, TrustedPartnersUpdateView
from admin_panel.views.services import ServicesCreateView, ServicesDeleteView, ServicesListView, ServicesUpdateView
from admin_panel.views.departments import DepartmentsCreateView, DepartmentsDeleteView, DepartmentsListView, DepartmentsUpdateView
from admin_panel.views.doctors import DoctorsCreateView, DoctorsDeleteView, DoctorsListView, DoctorsUpdateView



urlpatterns = [
    path("", AdminHomeView.as_view(), name="admin-index-page"),
    # AUTH VIEWS
    path("login/", AdminLoginView.as_view(), name="admin-login-page"),
    path("logout/", AdminLogoutView.as_view(), name="admin-logout-page"),

    # Home Page VIEWS

    path("banners/", BannerView.as_view(), name="admin-banner-page"),

    path("testimonials/", TestimonialListView.as_view(), name="admin-testimonials-page"),
    path("testimonials/create/", TestimonialCreateView.as_view(), name="admin-testimonials-create-page"),
    path("testimonials/update/<str:pk>", TestimonialUpdateView.as_view(), name="admin-testimonials-update-page"),
    path("testimonials/delete/<str:pk>", TestimonialDeleteView.as_view(), name="admin-testimonials-delete-page"),
    
    path("partners/", TrustedPartnersListView.as_view(), name="admin-partners-page"),
    path("partners/create/", TrustedPartnersCreateView.as_view(), name="admin-partners-create-page"),
    path("partners/update/<str:pk>", TrustedPartnersUpdateView.as_view(), name="admin-partners-update-page"),
    path("partners/delete/<str:pk>", TrustedPartnersDeleteView.as_view(), name="admin-partners-delete-page"),
    
    path("services/", ServicesListView.as_view(), name="admin-services-page"),
    path("services/create/", ServicesCreateView.as_view(), name="admin-services-create-page"),
    path("services/update/<str:pk>", ServicesUpdateView.as_view(), name="admin-services-update-page"),
    path("services/delete/<str:pk>", ServicesDeleteView.as_view(), name="admin-services-delete-page"),
    
    path("departments/", DepartmentsListView.as_view(), name="admin-departments-page"),
    path("departments/create/", DepartmentsCreateView.as_view(), name="admin-departments-create-page"),
    path("departments/update/<str:pk>", DepartmentsUpdateView.as_view(), name="admin-departments-update-page"),
    path("departments/delete/<str:pk>", DepartmentsDeleteView.as_view(), name="admin-departments-delete-page"),
    
    path("doctors/", DoctorsListView.as_view(), name="admin-doctors-page"),
    path("doctors/create/", DoctorsCreateView.as_view(), name="admin-doctors-create-page"),
    path("doctors/update/<str:pk>", DoctorsUpdateView.as_view(), name="admin-doctors-update-page"),
    path("doctors/delete/<str:pk>", DoctorsDeleteView.as_view(), name="admin-doctors-delete-page"),
    

    # 


]