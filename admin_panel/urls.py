from django.urls import path

from admin_panel.views.banners import BannerView
from admin_panel.views.common_views import AdminContactsDetailView, AdminContactsListView, AdminHomeView,AdminLoginView,AdminLogoutView
from admin_panel.views.testimonials import TestimonialCreateView, TestimonialDeleteView, TestimonialListView, TestimonialUpdateView
from admin_panel.views.trusted_partners import TrustedPartnersCreateView, TrustedPartnersDeleteView, TrustedPartnersListView, TrustedPartnersUpdateView
from admin_panel.views.services import ServicesCreateView, ServicesDeleteView, ServicesListView, ServicesUpdateView
from admin_panel.views.departments import (
    AppointmentsDetailView, DepartmentsCreateView, DepartmentsDeleteView, DepartmentsListView, DepartmentsUpdateView,
    AppointmentsListView,
)
from admin_panel.views.doctors import DoctorsCreateView, DoctorsDeleteView, DoctorsListView, DoctorsUpdateView
from admin_panel.views.blogs import ( 
    BlogCategoriesCreateView, BlogCategoriesDeleteView, BlogCategoriesListView, BlogCategoriesUpdateView,
    BlogTagsCreateView, BlogTagsDeleteView, BlogTagsListView, BlogTagsUpdateView,
    BlogsCreateView, BlogsDeleteView, BlogsListView, BlogsUpdateView,
)


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
    
    path("appointments/", AppointmentsListView.as_view(), name="admin-appointments-page"),
    path("appointments/<str:pk>", AppointmentsDetailView.as_view(), name="admin-appointments-detail-page"),

    path("contacts/", AdminContactsListView.as_view(), name="admin-contacts-page"),
    path("contacts/<str:pk>", AdminContactsDetailView.as_view(), name="admin-contacts-detail-page"),


    path("doctors/", DoctorsListView.as_view(), name="admin-doctors-page"),
    path("doctors/create/", DoctorsCreateView.as_view(), name="admin-doctors-create-page"),
    path("doctors/update/<str:pk>", DoctorsUpdateView.as_view(), name="admin-doctors-update-page"),
    path("doctors/delete/<str:pk>", DoctorsDeleteView.as_view(), name="admin-doctors-delete-page"),
    
    path("blog-categories/", BlogCategoriesListView.as_view(), name="admin-blog-cat-page"),
    path("blog-categories/create/", BlogCategoriesCreateView.as_view(), name="admin-blog-cat-create-page"),
    path("blog-categories/update/<str:pk>", BlogCategoriesUpdateView.as_view(), name="admin-blog-cat-update-page"),
    path("blog-categories/delete/<str:pk>", BlogCategoriesDeleteView.as_view(), name="admin-blog-cat-delete-page"),
    
    path("blog-tags/", BlogTagsListView.as_view(), name="admin-blog-tag-page"),
    path("blog-tags/create/", BlogTagsCreateView.as_view(), name="admin-blog-tag-create-page"),
    path("blog-tags/update/<str:pk>", BlogTagsUpdateView.as_view(), name="admin-blog-tag-update-page"),
    path("blog-tags/delete/<str:pk>", BlogTagsDeleteView.as_view(), name="admin-blog-tag-delete-page"),
    
    
    path("blogs/", BlogsListView.as_view(), name="admin-blog-page"),
    path("blogs/create/", BlogsCreateView.as_view(), name="admin-blog-create-page"),
    path("blogs/update/<str:pk>", BlogsUpdateView.as_view(), name="admin-blog-update-page"),
    path("blogs/delete/<str:pk>", BlogsDeleteView.as_view(), name="admin-blog-delete-page"),
    

    # 


]