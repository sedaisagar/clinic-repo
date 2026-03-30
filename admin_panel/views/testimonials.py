from django.views import generic

from mainapp.models import Testimonials
from django.urls import reverse_lazy
from django.contrib import messages

class TestimonialListView(generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Testimonials.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name", "position"]
        data["title"] = "Testimonials"
        return data


class TestimonialCreateView(generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Testimonials.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-testimonials-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Testimonial"
        return data

    def get_success_url(self):
        messages.success(self.request, "Testimonial Created Successfully!")
        return super().get_success_url()

class TestimonialUpdateView(generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Testimonials.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-testimonials-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Testimonial"
        return data

    def get_success_url(self):
        messages.success(self.request, "Testimonial Updated Successfully!")
        return super().get_success_url()

class TestimonialDeleteView(generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = Testimonials.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-testimonials-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Testimonial ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Testimonial Deleted Successfully!")
        return super().get_success_url()