from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from mainapp.models import TrustedPartners
from django.urls import reverse_lazy
from django.contrib import messages

class TrustedPartnersListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = TrustedPartners.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Trusted Partners"
        data["actions"] = ["create", "edit", "delete"]
        return data


class TrustedPartnersCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = TrustedPartners.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-partners-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Partner"
        return data

    def get_success_url(self):
        messages.success(self.request, "Partner Created Successfully!")
        return super().get_success_url()

class TrustedPartnersUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = TrustedPartners.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-partners-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Partner"
        return data

    def get_success_url(self):
        messages.success(self.request, "Partner Updated Successfully!")
        return super().get_success_url()

class TrustedPartnersDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = TrustedPartners.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-partners-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Partner ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Partner Deleted Successfully!")
        return super().get_success_url()