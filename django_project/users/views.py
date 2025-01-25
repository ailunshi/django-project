from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # create new instance with data from POST request
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}. You are now able to login.")
            return redirect("login")
    else:   
        form = UserRegisterForm() # create new instance
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

"""
get request: what you send when you navigate to the page normally
post request: where to post form data

options in messages:
messages.debug
messages.info
messages.success
messages.warning
messages.error
"""