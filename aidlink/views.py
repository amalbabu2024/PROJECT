from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth import get_user_model

from .models import User, Civilian, Coordinator

def register(request):
    return render(request,'signup.html')


def index(request):
    return render(request,'index.html')

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

        return redirect('/log')

    return render(request,'signup_coordinator.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            
            if user.is_civilian:
                return redirect('civilhome')  # Redirect to civilian home page
            elif user.is_coordinator:
                return redirect('coorhome')  # Redirect to coordinator home page
            else:
                return redirect('admindashboard')  # Redirect to admin dashboard or any other appropriate admin page
        else:
            messages.error(request, "Username or Password is Incorrect.")
    
    return render(request, 'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def civilian_home(request):
    return render(request, 'civilians_dashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def coordinator_home(request):
    return render(request, 'coordinators_dashboard.html')

def logo(request):
    # if request.user.is_authentcated:
    logout(request)
    return redirect('login')



def admindashboard(request):
    # You can add logic here to fetch data or perform other admin-related tasks
    return render(request, 'admindashboard.html')

def admindashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    users = User.objects.all()  # Query all users
    return render(request, 'admindashboard.html', {'users': users})

def admindashboard(request):
    civilians = Civilian.objects.all()
    return render(request, 'admindashboard.html', {'civilians': civilians})




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Civilian, Coordinator

def admindashboard(request):
    User = get_user_model()
    users = User.objects.all()
    civilians = Civilian.objects.all()
    coordinators = Coordinator.objects.all()
    
    context = {
        'users': users,
        'civilians': civilians,
        'coordinators': coordinators,
    }
    return render(request, 'admindashboard.html', context)

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






from django.shortcuts import render, redirect
from .forms import CoordinatorForm
from .models import User

def add_admin_coordinators(request):
    if request.method == 'POST':
        form = CoordinatorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user with the 'coordinator' role
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_coordinator = True
            user.save()

            # Optionally, you can add a success message here.
            return redirect('admindashboard')  # Redirect to the admin dashboard or the appropriate page.

    else:
        form = CoordinatorForm()

    return render(request, 'add_admin_coordinators.html', {'form': form})




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
        coordinator.contact_phone_number = request.POST.get('contact_phone_number')
        coordinator.verification = request.POST.get('verification_status')
        coordinator.registered_through_form = request.POST.get('registered_through_form')
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
from django.http import HttpResponse

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
            # Redirect or show success message
    else:
        form = ResourceForm()
    
    return render(request, 'add_resource.html', {'form': form})

from django.shortcuts import render
from .models import Resource

def view_resources(request):
    resources = Resource.objects.all()
    return render(request, 'view_resources.html', {'resources': resources})








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
