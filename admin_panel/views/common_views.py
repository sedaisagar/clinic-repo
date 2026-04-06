from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success

from admin_panel.forms.banner import SiteSettingsForm
from admin_panel.permissions import AdminLoginRequiredMixin
from admin_panel.forms import UserProfileForm, CustomPasswordChangeForm

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy

from mainapp.models import Contacts, SiteSettings
from users.models import User


class AdminLoginView(LoginView):
    template_name = "admin-panel/auth-login-basic.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "ADMIN":
            return redirect("admin-index-page")
        return super().dispatch(request, *args, **kwargs)


class AdminLogoutView(generic.TemplateView):
    template_name = "admin-panel/admin-logout-page.html"

    def post(self, request, *args, **kwargs):
        auth_logout(request) # This logs out the current login session
        return redirect("admin-login-page")


class AdminHomeView(AdminLoginRequiredMixin, generic.TemplateView):
    template_name = "admin-panel/index.html"



#  Contacts



# Appointments

class AdminContactsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Contacts.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name","email","subject","phone",]
        data["title"] = "Contacts"
        data["actions"] = ['detail']
        return data
        
class AdminContactsDetailView(AdminLoginRequiredMixin,generic.DetailView):
    template_name = "admin-panel/common/detail.html"
    queryset = Contacts.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name","email","subject","phone","message",]
        data["title"] = "Contact Details"
        data["list_name"] = "admin-contacts-page"
        return data


class AdminProfileView(AdminLoginRequiredMixin, generic.TemplateView):
    """View for displaying and updating admin user profile"""
    template_name = "admin-panel/admin-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if self.request.method == 'POST':
            # Handle form submission
            form_type = self.request.POST.get('form_type')
            
            if form_type == 'profile':
                profile_form = UserProfileForm(self.request.POST, instance=user)
                if profile_form.is_valid():
                    profile_form.save()
                    success(self.request, "Profile updated successfully!")
                context['profile_form'] = profile_form
                context['password_form'] = CustomPasswordChangeForm(user)
            
            elif form_type == 'password':
                password_form = CustomPasswordChangeForm(user, self.request.POST)
                if password_form.is_valid():
                    password_form.save()
                    success(self.request, "Password changed successfully!")
                context['password_form'] = password_form
                context['profile_form'] = UserProfileForm(instance=user)
        else:
            context['profile_form'] = UserProfileForm(instance=user)
            context['password_form'] = CustomPasswordChangeForm(user)
        
        context['user'] = user
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

# 
# Site Settings 
# 

from django.contrib import messages

class SiteSettingsView(AdminLoginRequiredMixin,generic.TemplateView):
    template_name = "admin-panel/common/forms.html"

    def get_object(self):
        return SiteSettings.objects.first() # Returns SiteSettings or None

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)

        data["title"] = "Site Settings Create / Update"

        instance = self.get_object()
        data["form"] = SiteSettingsForm(instance=instance)

        return data

    def post(self, request, *args, **kwargs):
        # Data, Files
        data, files = request.POST, request.FILES

        instance = self.get_object()

        if instance:
            # This is a update operation
            form = SiteSettingsForm(instance=instance, data=data, files=files)
        else:
            # This is create operation
            form = SiteSettingsForm(data=data, files=files)

        if form.is_valid():
            form.save()
            messages.success(request, "Settings Updated Successfully")
        else:
            messages.error(request, "Settings Not Updated", extra_tags="danger")
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)

        return redirect(self.request.get_full_path())