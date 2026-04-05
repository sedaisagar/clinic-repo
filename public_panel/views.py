from django.urls import reverse_lazy
from django.views import generic

from mainapp.models import Appointments, Banner, BlogCategories, BlogTags, Blogs, Contacts, Departments, Doctors, Services, Testimonials, TrustedPartners


class PublicHomeView(generic.TemplateView):
    template_name = "public/index.html"

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        
        data.update(
            banner = Banner.objects.first(),
            services = Services.objects.all()[:6],
            testimonials = Testimonials.objects.all(),
            partners = TrustedPartners.objects.all()
        )
        return data
class PublicAboutView(generic.TemplateView):
    template_name = "public/about.html"

class PublicServicesView(generic.TemplateView):
    template_name = "public/service.html"

class PublicDepartmentsView(generic.ListView):
    template_name = "public/department.html"
    queryset = Departments.objects.all()


class PublicDepartmentDetailView(generic.DetailView):
    template_name = "public/department-single.html"
    queryset = Departments.objects.all()


class PublicDoctorsView(generic.TemplateView):
    template_name = "public/doctor.html"

class PublicDoctorDetailView(generic.TemplateView):
    template_name = "public/doctor-single.html"


class PublicAppointmentView(generic.CreateView):
    template_name = "public/appointment.html"
    queryset = Appointments.objects.all()
    fields = "__all__"

    success_url = reverse_lazy("appointment-page")


    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["doctors"] = Doctors.objects.all()
        data["departments"] = Departments.objects.all()
        return data
        
class PublicBlogsView(generic.ListView):
    template_name = "public/blog-sidebar.html"
    queryset = Blogs.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["tags"]= BlogTags.objects.all()
        data["categories"]= BlogCategories.objects.all()
        return data
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        query_params = self.request.GET # DICT VALUES
        category = query_params.get("category")
        tag = query_params.get("tag")

        # Filter By Category
        if category:
            queryset = queryset.filter(category__pk=category)

        # Filter By Tag
        if tag:
            queryset = queryset.filter(tags__pk=tag)
        
        return queryset



class PublicBlogDetailView(generic.DetailView):
    template_name = "public/blog-single.html"
    queryset = Blogs.objects.all()


class PublicContactView(generic.CreateView):
    template_name = "public/contact.html"

    queryset = Contacts.objects.all()
    fields = "__all__"

    success_url = reverse_lazy("contact-page")
