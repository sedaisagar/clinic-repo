from mainapp.models import Banner, SiteSettings
from django import forms


class BannerForm(forms.ModelForm):

    class Meta:
        model = Banner
        fields = "__all__"
        
        # exclude = []
        # fields = []

class SiteSettingsForm(forms.ModelForm):

    class Meta:
        model = SiteSettings
        fields = "__all__"