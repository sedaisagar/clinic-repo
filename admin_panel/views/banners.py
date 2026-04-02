from django.shortcuts import redirect
from django.views import generic

from admin_panel.forms.banner import BannerForm
from admin_panel.permissions import AdminLoginRequiredMixin
from mainapp.models import Banner

from django.contrib import messages

class BannerView(AdminLoginRequiredMixin,generic.TemplateView):
    template_name = "admin-panel/common/forms.html"

    def get_object(self):
        return Banner.objects.first() # Returns Banner or None

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)

        data["title"] = "Banner Create / Update"

        instance = self.get_object()
        data["form"] = BannerForm(instance=instance)

        return data

    def post(self, request, *args, **kwargs):
        # Data, Files
        data, files = request.POST, request.FILES

        instance = self.get_object()

        if instance:
            # This is a update operation
            form = BannerForm(instance=instance, data=data, files=files)
        else:
            # This is create operation
            form = BannerForm(data=data, files=files)

        if form.is_valid():
            form.save()
            messages.success(request, "Banner Updated Successfully")
        else:
            messages.error(request, "Banner Not Updated", extra_tags="danger")
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)

        return redirect(self.request.get_full_path())