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
        fields = '__all__'
        # Add other fields as necessary





from django import forms
from .models import Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = '__all__'



# forms.py
from django import forms
from .models import MarkedLocation

class MarkedLocationForm(forms.ModelForm):
    class Meta:
        model = MarkedLocation
        fields = ['name', 'latitude', 'longitude']



# forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'priority', 'category']



# forms.py

from django import forms
from .models import HelpRequest

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['name', 'request_type', 'urgency_level', 'people_affected', 'details', 'attachments', 'language_preference', 'special_needs', 'relationship_to_situation', 'confirmation_checkbox', 'contact_number', 'current_location']




# forms.py
from django import forms
from .models import VolunteerRequest

class VolunteerRequestForm(forms.ModelForm):
    class Meta:
        model = VolunteerRequest
        exclude = ['user', 'status']
