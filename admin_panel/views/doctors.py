from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from mainapp.models import Doctors
from django.urls import reverse_lazy
from django.contrib import messages
from tinymce.widgets import TinyMCE

class DoctorsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Doctors.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Doctors"
        data["actions"] = ["create", "edit", "delete"]

        return data


class DoctorsCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Doctors.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-doctors-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Doctor"
        return data

    def get_success_url(self):
        messages.success(self.request, "Doctor Created Successfully!")
        return super().get_success_url()

    def get_form(self):
        form =  super().get_form()
        form.fields['doctors_intro'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form

class DoctorsUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Doctors.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-doctors-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Doctor"
        return data

    def get_success_url(self):
        messages.success(self.request, "Doctor Updated Successfully!")
        return super().get_success_url()

    def get_form(self):
        form =  super().get_form()
        form.fields['doctors_intro'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form

class DoctorsDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = Doctors.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-doctors-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Doctor ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Doctor Deleted Successfully!")
        return super().get_success_url()