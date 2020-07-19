from django.forms import ModelForm
from django import forms
from .models import Allergy
from .models import Hospitalization



class AllergyForm(ModelForm):
    class Meta:
        model = Allergy
        fields = ['New_Allergy', 'description', 'Life_threatening']


class HospitalizationForm(ModelForm):
    class Meta:
        model = Hospitalization
        fields = ['Name_of_hospital', 'description']



    