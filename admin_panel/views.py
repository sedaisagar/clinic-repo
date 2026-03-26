from django.views import generic


class AdminHomeView(generic.TemplateView):
    template_name = "admin-panel/index.html"