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











from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


# forms.py

from django import forms
from .models import Organization_Resources

class OrganizationResourcesForm(forms.ModelForm):
    class Meta:
        model = Organization_Resources
        fields = ['ResourceName', 'Description', 'Quantity', 'ResourceType']




# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'deadline']




from django import forms

class DonationForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=1)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15)



from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration_in_weeks', 'start_date', 'end_date', 'instructor']



from django import forms

class AdminAlertForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
