from django import forms

from mainapp.models import Departments

class FeaturesForm(forms.Form):
    feature = forms.CharField()

class SchedulesForm(forms.Form):
    days = forms.CharField()
    hours = forms.CharField()


from django.forms import formset_factory

FeaturesForms = formset_factory(FeaturesForm, min_num=1, extra=1, max_num=10)
SchedulesForms = formset_factory(SchedulesForm, min_num=1, extra=1, max_num=10)

class DepartmentForm(forms.ModelForm):
    helpline_number = forms.CharField() # extra fields added 

    class Meta:
        model = Departments
        exclude = ["extra_info"]

    def clean(self):
        cleaned_data = super().clean()

        ffs = FeaturesForms(data=self.data, prefix='features')
        sfs = SchedulesForms(data=self.data,  prefix='schedules')

        schedules, features = [], []

        if ffs.is_valid() and sfs.is_valid():
            schedules = sfs.cleaned_data
            features = ffs.cleaned_data            
        else:
            if self.instance:
                schedules = self.instance.extra_info.get("schedules", [])
                features = self.instance.extra_info.get("features", [])


        helpline_number = cleaned_data.pop("helpline_number", "")
        cleaned_data["extra_info"] = {
            "schedules": schedules,
            "features":features,
            "helpline_number": helpline_number,
        }
        return cleaned_data

    def save(self, commit = ...):
        instance:Departments = super().save(commit)
        
        instance.extra_info = self.cleaned_data.get("extra_info")
        instance.save(update_fields=["extra_info"])

        return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["helpline_number"].initial = self.instance.extra_info.get("helpline_number", "")

