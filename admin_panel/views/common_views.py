from django.shortcuts import redirect
from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout

from mainapp.models import Contacts


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


