from django import forms

class CoordinatorForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)  # You may want to use a more secure way to store passwords



from django import forms
from .models import Coordinator

class CoordinatorProfileEditForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__'



from django import forms
from .models import Civilian

class CivilianProfileEditForm(forms.ModelForm):
    class Meta:
        model = Civilian
        fields = '__all__'






from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'type', 'quantity']
        # Add other fields as necessary
