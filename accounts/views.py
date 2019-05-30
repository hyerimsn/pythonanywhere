from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid:
            signup_form.save()
            return redirect('index')
        else:
            return redirect('signup')

    signup_form = UserCreationForm()
    return render(request, 'registration/signup.html',{'signup_form':signup_form})