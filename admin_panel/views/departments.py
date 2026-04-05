from django.views import generic

from admin_panel.forms.departments import DepartmentForm, FeaturesForms, SchedulesForms
from admin_panel.permissions import AdminLoginRequiredMixin
from mainapp.models import Departments, Appointments
from django.urls import reverse_lazy
from django.contrib import messages

class DepartmentsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Departments.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Departments"
        data["actions"] = ["create", "edit", "delete"]
        return data


class DepartmentsCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Departments.objects.all()
    # fields = "__all__"
    form_class = DepartmentForm
    success_url = reverse_lazy("admin-departments-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Department"
        data["formsets"] = [
            {
                "title":"Schedules",
                "prefix": "schedules",
                "formset": SchedulesForms(prefix='schedules'),
            },{
                "title":"Features",
                "prefix": "features",
                "formset": FeaturesForms(prefix='features'),
            },
        ]
        return data

    def get_success_url(self):
        messages.success(self.request, "Department Created Successfully!")
        return super().get_success_url()

class DepartmentsUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Departments.objects.all()
    # fields = "__all__"
    form_class = DepartmentForm

    success_url = reverse_lazy("admin-departments-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Department"
        data["formsets"] = [
            {
                "title":"Schedules",
                "prefix": "schedules",
                "formset": SchedulesForms(prefix='schedules', initial=self.object.extra_info.get("schedules", [])),
            },{
                "title":"Features",
                "prefix": "features",
                "formset": FeaturesForms(prefix='features', initial=self.object.extra_info.get("features", [])),
            },
        ]
        return data

    def get_success_url(self):
        messages.success(self.request, "Department Updated Successfully!")
        return super().get_success_url()

class DepartmentsDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = Departments.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-departments-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Department ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Department Deleted Successfully!")
        return super().get_success_url()


# Appointments

class AppointmentsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Appointments.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["full_name", "department", "doctor", "appointment_date", "appointment_time"]
        data["title"] = "Appointments"
        # data["actions"] = ["create", "edit", "delete"]
        data["actions"] = ['detail']
        return data
        
class AppointmentsDetailView(AdminLoginRequiredMixin,generic.DetailView):
    template_name = "admin-panel/common/detail.html"
    queryset = Appointments.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["user", "full_name", "department", "doctor", "appointment_date", "appointment_time", "message"]
        data["title"] = "Appointment Details"
        data["list_name"] = "admin-appointments-page"
        return data


