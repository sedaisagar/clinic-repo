from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView,  LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from mainapp.models import Appointments, Banner, BlogCategories, BlogTags, Blogs, Contacts, Departments, Doctors, Services, Testimonials, TrustedPartners
from users.models import User


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


# ------ DASHBOARD VIEWS ------

class DashboardLoginView(LoginView):
    """User/Patient Login View"""
    template_name = "public/dashboard/login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("dashboard-index")


from django import forms
from django.contrib.auth.hashers import make_password
class UserRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',]

class DashboardRegisterView(generic.TemplateView):
    """User/Patient Registration View"""
    template_name = "public/dashboard/register.html"
    
    success_url = reverse_lazy("dashboard-login")
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        form = UserRegForm(data=request.POST)
        if form.is_valid():

            # Validation
            if not all([first_name, last_name, email, username, password1, password2]):
                messages.error(request, "All fields are required.")
                return self.get(request, *args, **kwargs)
            
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return self.get(request, *args, **kwargs)
            
            if len(password1) < 8:
                messages.error(request, "Password must be at least 8 characters long.")
                return self.get(request, *args, **kwargs)
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return self.get(request, *args, **kwargs)
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return self.get(request, *args, **kwargs)
            
        
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('dashboard-login')
        else:
            breakpoint()
            messages.error(request, f"Error creating account")
            context = self.get_context_data(**kwargs)
            context.update(
                form = form,
            )
            return self.render_to_response(context)


class DashboardIndexView(LoginRequiredMixin, generic.TemplateView):
    """User Dashboard View"""
    template_name = "public/dashboard/index.html"
    login_url = "dashboard-login"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Get user's appointments
        context['appointments'] = Appointments.objects.filter(full_name=user.get_full_name()).order_by('-appointment_date')[:5]
        context['user'] = user
        
        return context


class DashboardLogoutView(LogoutView):
    """User/Patient Logout View"""
    next_page = reverse_lazy("dashboard-login")


