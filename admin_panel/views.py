from django.shortcuts import redirect
from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout


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