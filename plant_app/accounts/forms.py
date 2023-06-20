
from django import forms

from plant_app.accounts.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"
