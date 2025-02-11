from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect("profile")
            # post/redirect/get pattern - not redirecting (above) means attempts to refresh the server response can cause contents of original POST to be resubmitted
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "users/profile.html", context)

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