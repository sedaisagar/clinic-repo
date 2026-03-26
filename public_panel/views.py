from django.views import generic


class PublicHomeView(generic.TemplateView):
    template_name = "public/index.html"

class PublicAboutView(generic.TemplateView):
    template_name = "public/about.html"