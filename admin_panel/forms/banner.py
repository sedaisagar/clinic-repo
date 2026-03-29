from mainapp.models import Banner
from django import forms


class BannerForm(forms.ModelForm):

    class Meta:
        model = Banner
        fields = "__all__"
        
        # exclude = []
        # fields = []