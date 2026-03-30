from django.views import generic

from mainapp.models import Services
from django.urls import reverse_lazy
from django.contrib import messages

class ServicesListView(generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Services.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["title"]
        data["title"] = "Services"
        return data


class ServicesCreateView(generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Services.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-services-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Service"
        return data

    def get_success_url(self):
        messages.success(self.request, "Service Created Successfully!")
        return super().get_success_url()

class ServicesUpdateView(generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Services.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-services-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Service"
        return data

    def get_success_url(self):
        messages.success(self.request, "Service Updated Successfully!")
        return super().get_success_url()

class ServicesDeleteView(generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = Services.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-services-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Service ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Service Deleted Successfully!")
        return super().get_success_url()