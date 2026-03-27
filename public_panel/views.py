from django.views import generic


class PublicHomeView(generic.TemplateView):
    template_name = "public/index.html"

class PublicAboutView(generic.TemplateView):
    template_name = "public/about.html"

class PublicServicesView(generic.TemplateView):
    template_name = "public/service.html"

class PublicDepartmentsView(generic.TemplateView):
    template_name = "public/department.html"

class PublicDepartmentDetailView(generic.TemplateView):
    template_name = "public/department-single.html"

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
