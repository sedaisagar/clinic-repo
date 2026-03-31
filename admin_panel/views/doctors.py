from django.views import generic

from mainapp.models import Doctors
from django.urls import reverse_lazy
from django.contrib import messages

class DoctorsListView(generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Doctors.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Doctors"
        return data


class DoctorsCreateView(generic.CreateView):
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

class DoctorsUpdateView(generic.UpdateView):
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

class DoctorsDeleteView(generic.DeleteView):
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