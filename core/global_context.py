

from mainapp.models import SiteSettings


def site_settings(request):
    return {"ss": SiteSettings.objects.first()}
