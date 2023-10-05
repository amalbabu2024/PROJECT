from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def index(request):
    return render(request, "index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            # Use filter to check if a user with the given username and password exists
            user = UserProfile.objects.filter(username=username, password=password).first()
        
            if user is not None:
                # Assuming you have a session key 'username' to store the username
                request.session["username"] = user.username
                
                # Redirect to the dashboard or any other page
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid Username or Password.")
                return redirect('/login')
    
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        # Get user input from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Perform form validation (server-side) as needed
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('signup')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create a new user profile model instance and save it to the database
        user_profile = UserProfile(username=username, email=email, password=password)
        user_profile.save()

        # Optionally, you can log in the user after registration
        # auth_login(request, user_profile)  # Import auth_login if not already imported

        return redirect('login')  # Redirect to the login page after successful signup

    return render(request, 'signup.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
#    return render(request,'dashboard.html')
def user_logout(request):
    return redirect('index',)

