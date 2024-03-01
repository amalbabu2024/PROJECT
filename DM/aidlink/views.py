from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth import get_user_model
from .models import User, Civilian, Coordinator
from .models import Manager,Organization,TeamLeader,TeamMember

def index(request):
    return render(request,'index.html')

def admindashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    User = get_user_model()
    users = User.objects.all()
    civilians = Civilian.objects.all()
    coordinators = Coordinator.objects.all()
    managers = Manager.objects.all()
    team_leaders = TeamLeader.objects.all()
    team_members = TeamMember.objects.all()
    
    context = {
        'users': users,
        'civilians': civilians,
        'coordinators': coordinators,
        'managers': managers,
        'team_leaders': team_leaders,
        'team_members': team_members,
    }
    return render(request, 'admindashboard.html', context)


def civreg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.success(request,("Username is already taken."))
            return render(request, 'signup_civilian.html')

        user = User(username=username, email=email, is_civilian=True)
        user.set_password(password)
        user.save()

        civilian = Civilian(user=user)
        civilian.save()

        return redirect('/log')

    return render(request,'signup_civilian.html')

def cooreg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.success(request,("Username is already taken."))
            return render(request, 'singup_coordinator.html')

        user = User(username=username, email=email, is_coordinator=True)
        user.set_password(password)
        user.save()

        coordinator = Coordinator(user=user)
        coordinator.save()

        return redirect('/admindashboard')

    return render(request,'signup_coordinator.html')

@login_required(login_url='login')
def managerreg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        organization_id = request.POST.get('organization')  # Retrieve selected organization ID

        if User.objects.filter(username=username).exists():
            messages.success(request, "Username is already taken.")
            return render(request, 'signup_manager.html')

        user = User(username=username, email=email, is_manager=True)
        user.set_password(password)
        user.save()

        organization = None
        if organization_id:
            organization = Organization.objects.get(OrganizationID=organization_id)  # Corrected field name

        manager = Manager(user=user, organization=organization)  # Assign organization to manager
        manager.save()

        return redirect('/admindashboard')

    organizations = Organization.objects.all()
    return render(request, 'signup_manager.html', {'organizations': organizations})

def team_leader_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        organization_id = request.POST.get('organization')

        if User.objects.filter(username=username).exists():
            messages.success(request, "Username is already taken.")
            return render(request, 'signup_team_leader.html')

        user = User(username=username, email=email, is_team_leader=True)
        user.set_password(password)
        user.save()

        organization = None
        if organization_id:
            organization = Organization.objects.get(OrganizationID=organization_id)
        
        manager_id = request.user.id

        team_leader = TeamLeader(user=user, organization=organization, manager_id=manager_id)
        team_leader.save()

        return redirect('/managerdashboard')  # Redirect to appropriate dashboard

    organizations = Organization.objects.all()
    return render(request, 'signup_team_leader.html', {'organizations': organizations})

def team_member_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        organization_id = request.POST.get('organization')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('team_member_registration')

        user = User(username=username, email=email, is_team_member=True)
        user.set_password(password)
        user.save()

        organization = None
        if organization_id:
            organization = Organization.objects.get(OrganizationID=organization_id)
            
        team_leader_id = request.user.id

        team_member = TeamMember(user=user, organization=organization, team_leader_id=team_leader_id)
        team_member.save()

        return redirect('/teamleaderdashboard')  # Redirect to appropriate dashboard

    organizations = Organization.objects.all()
    return render(request, 'signup_team_member.html', {'organizations': organizations})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            
            if user.is_admin:
                return redirect('admindashboard')
            elif user.is_civilian:
                return redirect('civilhome')  # Redirect to civilian home page
            elif user.is_coordinator:
                return redirect('coorhome')  # Redirect to coordinator home page
            elif user.is_manager:
                return redirect('manager_dashboard')
            elif user.is_team_leader:
                return redirect('team_leader_dashboard')
            elif user.is_team_member:
                return redirect('team_member_dashboard')
            else:
                return redirect('log')  
        else:
            messages.error(request, "Username or Password is Incorrect.")
    
    return render(request, 'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def admin_home(request):
    return render(request, 'admindashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def civilian_home(request):
    return render(request, 'civilians_dashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def coordinator_home(request):
    return render(request, 'coordinators_dashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def manager_home(request):
    return render(request, 'manager_dashboard.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def team_leader_home(request):
    return render(request, 'team_leader_dashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def team_member_home(request):
    return render(request, 'team_member_dashboard.html')

def logo(request):
    # if request.user.is_authentcated:
    logout(request)
    return redirect('login')





from django.shortcuts import render
from .models import User

def admin_view_users(request):
    users = User.objects.all()
    return render(request, 'admin_view_users.html', {'users': users})

from django.shortcuts import render
from .models import Civilian

def admin_view_civilians(request):
    civilians = Civilian.objects.all()
    return render(request, 'admin_view_civilians.html', {'civilians': civilians})






from .models import Coordinator, User

def admin_view_coordinators(request):
    coordinators = Coordinator.objects.all()
    admin_added_coordinators = Coordinator.objects.filter(registered_through_form=False)
    return render(request, 'admin_view_coordinators.html', {'coordinators': coordinators, 'admin_added_coordinators': admin_added_coordinators})






from django.shortcuts import render
from .models import Coordinator

def coordinators_profile(request):
    # Get the current coordinator's profile
    coordinator = Coordinator.objects.get(user=request.user)

    return render(request, 'coordinators_profile.html', {'coordinator': coordinator})


from django.shortcuts import render, redirect
from .models import Coordinator

def edit_coordinator_profile(request):
    coordinator = Coordinator.objects.get(user=request.user)

    if request.method == 'POST':
        coordinator.first_name = request.POST.get('first_name')
        coordinator.last_name = request.POST.get('last_name')
        coordinator.contact_email = request.POST.get('contact_email')
        coordinator.contact_phone_number = request.POST.get('contact_phone_number')
        coordinator.save()
        return redirect('coordinators_profile')  # Redirect to the coordinator profile page after saving the changes

    return render(request, 'edit_coordinator_profile.html', {'coordinator': coordinator})







from django.shortcuts import render
from .models import Civilian

def civilian_profile(request):
    # Assuming you pass the civilian instance to the template
    civilian = Civilian.objects.get(user=request.user)
    return render(request, 'civilian_profile.html', {'civilian': civilian})


from django.shortcuts import render, redirect
from .models import Civilian

def edit_civilian_profile(request):
    civilian = Civilian.objects.get(user=request.user)

    if request.method == 'POST':
        civilian.first_name = request.POST.get('first_name')
        civilian.last_name = request.POST.get('last_name')
        civilian.phone_number = request.POST.get('phone_number')
        civilian.country = request.POST.get('country')
        civilian.gender = request.POST.get('gender')
        civilian.save()
        return redirect('civilian_profile')  # Redirect to the civilian profile page after saving the changes

    return render(request, 'edit_civilian_profile.html', {'civilian': civilian})






from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest

@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if request.user.check_password(current_password):
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Update the user's session hash
                messages.success(request, "Password changed successfully.")
                return redirect("password_change_success")
            else:
                messages.error(request, "New password and confirmation password do not match.")
                return HttpResponse("New password and confirmation password do not match.", status=400)
        else:
            messages.error(request, "Current password is incorrect.")
            return HttpResponse("Current password is incorrect.", status=400)

    return render(request, "change_password.html")

def password_change_success(request):
    return render(request, 'password_change_success.html')






from django.shortcuts import render
from .forms import ResourceForm

def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('view_resources') # Redirect or show success message
    else:
        form = ResourceForm()
    return render(request, 'add_resource.html', {'form': form})

from django.shortcuts import render
from .models import Resource

def view_resources(request):
    resources = Resource.objects.all()
    return render(request, 'view_resources.html', {'resources': resources})

def edit_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('view_resources')
    else:
        form = ResourceForm(instance=resource)
    
    return render(request, 'edit_resource.html', {'form': form, 'resource': resource})

def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    
    if request.method == 'POST':
        resource.delete()
        return redirect('view_resources')
    
    return render(request, 'delete_resource.html', {'resource': resource})








from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def change_coordinator_status(request, coordinator_id):
    if request.method == 'POST':
        User = get_user_model()
        coordinator = User.objects.get(id=coordinator_id)
        new_status = request.POST.get('status')

        if new_status == 'active':
            coordinator.is_active = True
            send_activation_email(coordinator)
        elif new_status == 'inactive':
            coordinator.is_active = False
            send_deactivation_email(coordinator)

        coordinator.save()
        messages.success(request, f'Status for {coordinator.username} has been changed to {new_status}.')
    
    return redirect('admin_view_coordinators')


def send_activation_email(user):
    subject = "Your Account Activation"
    from_email = "your-email@example.com"  # Update with your email
    recipient_list = [user.email]

    context = {'user': user}
    html_message = render_to_string('activation_email.html', context)

    msg = EmailMultiAlternatives(subject, strip_tags(html_message), from_email, recipient_list)
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def send_deactivation_email(user):
    subject = "Your Account Deactivation"
    from_email = "your-email@example.com"  # Update with your email
    recipient_list = [user.email]

    context = {'user': user}
    html_message = render_to_string('deactivation_email.html', context)

    msg = EmailMultiAlternatives(subject, strip_tags(html_message), from_email, recipient_list)
    msg.attach_alternative(html_message, "text/html")
    msg.send()



def change_civilian_status(request, civilian_id):
    if request.method == 'POST':
        User = get_user_model()
        civilian = User.objects.get(id=civilian_id)
        new_status = request.POST.get('status')

        if new_status == 'active':
            civilian.is_active = True
            send_activation_email(civilian)
        elif new_status == 'inactive':
            civilian.is_active = False
            send_deactivation_email(civilian)

        civilian.save()
        messages.success(request, f'Status for {civilian.username} has been changed to {new_status}.')
    
    return redirect('admin_view_civilians')







from django.shortcuts import render, redirect
from .models import Camp
from .forms import CampForm

# View to add a camp
def add_camp(request):
    if request.method == 'POST':
        form = CampForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_location')
    else:
        form = CampForm()
    return render(request, 'add_camp.html', {'form': form})


from django.shortcuts import render
from .models import Camp

def view_camps(request):
    camps = Camp.objects.all()
    return render(request, 'view_camps.html', {'camps': camps})



# views.py
from django.shortcuts import render, redirect
from .models import MarkedLocation
from .forms import MarkedLocationForm

def add_location(request):
    if request.method == 'POST':
        form = MarkedLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_locations')
    else:
        form = MarkedLocationForm()

    return render(request, 'add_location.html', {'form': form})

def view_locations(request):
    locations = MarkedLocation.objects.all()
    return render(request, 'view_locations.html', {'locations': locations})




# views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()

    return render(request, 'add_message.html', {'form': form})

def message_list(request):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'message_list.html', {'messages': messages})




# # views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Civilian, HelpRequest
from .forms import HelpRequestForm

@login_required
def send_help_request(request):
    civilian = Civilian.objects.get(user=request.user)

    if request.method == 'POST':
        form = HelpRequestForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form data to the HelpRequest model
            help_request = form.save(commit=False)
            help_request.civilian = civilian.user  # Assign the User instance
            help_request.save()

            messages.success(request, "Help request submitted successfully.")
            return redirect('view_help_requests')

    else:
        form = HelpRequestForm()

    return render(request, 'send_help_request.html', {'form': form})





from django.db.models import Q

def view_help_requests(request):
    help_requests = HelpRequest.objects.all().order_by('-timestamp')

    if 'search' in request.GET:
        search_query = request.GET.get('search', '')
        if search_query:
            help_requests = help_requests.filter(
                Q(name__icontains=search_query) |
                Q(request_type__icontains=search_query) |
                Q(urgency_level__icontains=search_query) |
                Q(people_affected__icontains=search_query) |
                Q(details__icontains=search_query) |
                Q(language_preference__icontains=search_query) |
                Q(special_needs__icontains=search_query) |
                Q(relationship_to_situation__icontains=search_query) |
                Q(contact_number__icontains=search_query) |
                Q(current_location__icontains=search_query)
            )

    return render(request, 'view_help_requests.html', {'help_requests': help_requests})






from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HelpRequest


# views.py

from django.shortcuts import render
from .models import HelpRequest

def view_help_requests(request):
    # Filter help requests based on the currently logged-in civilian
    help_requests = HelpRequest.objects.filter(civilian=request.user)

    return render(request, 'view_help_requests.html', {'help_requests': help_requests})

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import HelpRequest
from .forms import HelpRequestForm  # Assuming you have a form for editing help requests

def edit_help_request(request, request_id):
    help_request = get_object_or_404(HelpRequest, id=request_id)

    if request.method == 'POST':
        form = HelpRequestForm(request.POST, instance=help_request)
        if form.is_valid():
            form.save()
            return redirect('view_help_requests')
    else:
        form = HelpRequestForm(instance=help_request)

    return render(request, 'edit_help_request.html', {'form': form, 'help_request': help_request})

def delete_help_request(request, request_id):
    help_request = get_object_or_404(HelpRequest, id=request_id)
    
    if request.method == 'POST':
        help_request.delete()
        return redirect('view_help_requests')

    return render(request, 'delete_help_request.html', {'help_request': help_request})











from django.shortcuts import render
from .models import HelpRequest

def coordinator_view(request):
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', '')

    help_requests = HelpRequest.objects.all()

    # Apply category filter if selected
    if category_filter:
        help_requests = help_requests.filter(urgency_level=category_filter)

    # Apply status filter if selected
    if status_filter:
        help_requests = help_requests.filter(request_status=status_filter)

    return render(request, 'coordinator_view.html', {'help_requests': help_requests})




# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HelpRequest

def set_request_status(request, request_id):
    if request.method == 'POST':
        # Retrieve the HelpRequest object based on request_id
        help_request = HelpRequest.objects.get(pk=request_id)

        # Update the request status based on the form data
        new_status = request.POST.get('status')
        help_request.request_status = new_status
        help_request.save()

        messages.success(request, f"Request status updated to {new_status}.")

    return redirect('coordinator_view')  # Redirect to the coordinator_view page




from django.shortcuts import render
from .models import HelpRequest

def coordinator_view(request):
    # Get filter parameters from the request
    urgency_level = request.GET.get('urgency_level', '')
    status = request.GET.get('status', '')

    # Filter help requests based on urgency level and status
    help_requests = HelpRequest.objects.all()

    if urgency_level:
        help_requests = help_requests.filter(urgency_level=urgency_level)

    if status:
        help_requests = help_requests.filter(request_status=status)

    # Render the template with the filtered help requests
    return render(request, 'coordinator_view.html', {'help_requests': help_requests})






# views.py
from django.shortcuts import render, redirect
from .models import VolunteerRequest
from .forms import VolunteerRequestForm

def volunteer_request(request):
    if request.method == 'POST':
        form = VolunteerRequestForm(request.POST)
        if form.is_valid():
            volunteer_request = form.save(commit=False)
            volunteer_request.user = request.user
            volunteer_request.save()
            return redirect('volunteer_request_success')
    else:
        form = VolunteerRequestForm()

    return render(request, 'volunteer_request.html', {'form': form})

def volunteer_request_success(request):
    return render(request, 'volunteer_request_success.html')


# views.py
from django.shortcuts import render
from .models import VolunteerRequest

def manage_volunteer_requests(request):
    volunteer_requests = VolunteerRequest.objects.all()
    return render(request, 'manage_volunteer_requests.html', {'volunteer_requests': volunteer_requests})


from django.shortcuts import render
from .models import VolunteerRequest

def view_volunteer_request(request, request_id):
    volunteer_request = VolunteerRequest.objects.get(id=request_id)
    return render(request, 'view_volunteer_request.html', {'volunteer_request': volunteer_request})


# In your views.py file

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import VolunteerRequest

def update_volunteer_status(request, request_id):
    volunteer_request = get_object_or_404(VolunteerRequest, id=request_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        volunteer_request.status = new_status
        volunteer_request.save()

    return HttpResponseRedirect('/manage_volunteer_requests/')  # Redirect to the manage_volunteer_requests page






# views.py
from django.shortcuts import render
from .models import VolunteerRequest

def view_civilian_request(request):
    # Assuming you have a way to identify the civilian user (e.g., through authentication)
    # Replace 'your_civilian_user' with the actual way you identify the civilian user
    volunteer_requests = VolunteerRequest.objects.filter(user=request.user)

    context = {
        'volunteer_requests': volunteer_requests,
    }

    return render(request, 'view_civilian_request.html', context)


















from django.shortcuts import render, redirect
from .forms import OrganizationForm

@login_required(login_url='login')
def admin_add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('managerreg')  # Redirect to the same page after successful form submission
    else:
        form = OrganizationForm()
    return render(request, 'admin_add_organization.html', {'form': form})

@login_required
def manager_profile(request):
    manager = Manager.objects.get(user=request.user.manager)
    context = {'manager': manager}
    return render(request, 'manager_profile.html', context)


from django.shortcuts import render, redirect
from .models import Manager

@login_required
def edit_manager_profile(request):
    manager = Manager.objects.get(user=request.user)

    if request.method == 'POST':
        manager.first_name = request.POST.get('first_name')
        manager.last_name = request.POST.get('last_name')
        manager.contact_email = request.POST.get('contact_email')
        manager.contact_phone_number = request.POST.get('contact_phone_number')
        manager.save()
        return redirect('manager_profile')  # Redirect to the manager profile page after saving the changes

    return render(request, 'edit_manager_profile.html', {'manager': manager})



from django.shortcuts import render, redirect
from .models import TeamLeader

@login_required
def team_leader_profile(request):
    team_leader = TeamLeader.objects.get(user=request.user)
    return render(request, 'team_leader_profile.html', {'team_leader': team_leader})

@login_required
def edit_team_leader_profile(request):
    team_leader = TeamLeader.objects.get(user=request.user)

    if request.method == 'POST':
        team_leader.first_name = request.POST.get('first_name')
        team_leader.last_name = request.POST.get('last_name')
        team_leader.contact_email = request.POST.get('contact_email')
        team_leader.contact_phone_number = request.POST.get('contact_phone_number')
        team_leader.save()
        return redirect('team_leader_profile')  # Redirect to the team leader profile page after saving the changes

    return render(request, 'edit_team_leader_profile.html', {'team_leader': team_leader})


from django.shortcuts import render, redirect
from .models import TeamMember
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def team_member_profile(request):
    team_member = TeamMember.objects.get(user=request.user)
    return render(request, 'team_member_profile.html', {'team_member': team_member})

@login_required(login_url='login')
def edit_team_member_profile(request):
    team_member = TeamMember.objects.get(user=request.user)

    if request.method == 'POST':
        team_member.first_name = request.POST.get('first_name')
        team_member.last_name = request.POST.get('last_name')
        team_member.contact_email = request.POST.get('contact_email')
        team_member.contact_phone_number = request.POST.get('contact_phone_number')
        team_member.save()
        return redirect('team_member_profile')  # Redirect to the team member profile page after saving the changes

    return render(request, 'edit_team_member_profile.html', {'team_member': team_member})



from django.shortcuts import render, redirect
from .models import Organization_Resources
from .forms import OrganizationResourcesForm
from .models import Organization, User, Coordinator, Manager, TeamLeader, TeamMember

def add_organization_resources(request):
    if request.method == 'POST':
        form = OrganizationResourcesForm(request.POST)
        if form.is_valid():
            user_id = request.user.id

            if Coordinator.objects.filter(user_id=user_id).exists():
                coordinator = Coordinator.objects.get(user_id=user_id)
                organization = coordinator.organization
            elif Manager.objects.filter(user_id=user_id).exists():
                manager = Manager.objects.get(user_id=user_id)
                organization = manager.organization
            elif TeamLeader.objects.filter(user_id=user_id).exists():
                team_leader = TeamLeader.objects.get(user_id=user_id)
                organization = team_leader.organization
            elif TeamMember.objects.filter(user_id=user_id).exists():
                team_member = TeamMember.objects.get(user_id=user_id)
                organization = team_member.organization
            else:
                return redirect('error')  # Handle the case where user role is not found
            
            # Add Organization Resources fields to the form data
            form.instance.OrganizationID = organization
            form.save()
            return redirect('view_organization_resources')  # Redirect to a success page
    else:
        form = OrganizationResourcesForm()
    
    return render(request, 'add_organization_resources.html', {'form': form})



from django.shortcuts import render
from .models import Organization_Resources

def view_organization_resources(request):
    user_organization_id = request.user.team_leader.organization.OrganizationID
    organization_resources = Organization_Resources.objects.filter(OrganizationID=user_organization_id)
    context = {
        'organization_resources': organization_resources
    }
    return render(request, 'organization_resources.html', context)


from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

from .models import TeamLeader, TeamMember

def manager_assign_task(request, user_id):
    team_leaders = TeamLeader.objects.filter(manager_id=user_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            assigned_to_id = request.POST.get('assigned_to')
            task.assigned_to_id = assigned_to_id
            task.save()
            return redirect('manager_task_list')
    else:
        form = TaskForm()
    return render(request, 'manager_assign_task.html', {'form': form, 'team_leaders': team_leaders})



def manager_task_list(request):
    tasks = Task.objects.filter(assigned_by=request.user)
    return render(request, 'manager_task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

from .models import TeamLeader

def team_leader_assign_task(request, user_id):
    team_members = TeamMember.objects.filter(team_leader_id=user_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            assigned_to_id = request.POST.get('assigned_to')
            task.assigned_to_id = assigned_to_id
            task.save()
            return redirect('team_leader_dashboard')
    else:
        form = TaskForm()
    return render(request, 'team_leader_assign_task.html', {'form': form, 'team_members': team_members})

def team_leader_task_list(request, user_id):
    tasks_assigned_by_team_leader = Task.objects.filter(assigned_by=user_id)
    tasks_assigned_to_team_leader = Task.objects.filter(assigned_to=user_id)
    return render(request, 'team_leader_task_list.html', {'tasks_assigned_by_team_leader': tasks_assigned_by_team_leader, 'tasks_assigned_to_team_leader': tasks_assigned_to_team_leader})


def team_member_task_list(request):
    tasks_assigned_to_team_member = Task.objects.filter(assigned_to=request.user)
    return render(request, 'team_member_task_list.html', {'tasks_assigned_to_team_member': tasks_assigned_to_team_member})


def update_task_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
        return redirect('team_member_task_list')
    return render(request, 'update_task_status.html', {'task': task})
