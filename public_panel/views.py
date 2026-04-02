from django.views import generic

from mainapp.models import Banner, Departments, Services, Testimonials, TrustedPartners


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


class PublicAppointmentView(generic.TemplateView):
    template_name = "public/appointment.html"


class PublicBlogsView(generic.TemplateView):
    template_name = "public/blog-sidebar.html"

class PublicBlogDetailView(generic.TemplateView):
    template_name = "public/blog-single.html"


class PublicContactView(generic.TemplateView):
    template_name = "public/contact.html"
