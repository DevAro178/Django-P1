from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registerForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Welcome {username}, your account has been created."
            )
            form.save()
            return redirect("login")
    else:
        form = registerForm()
    context = {"form": form}
    return render(request, "users/register.html", context)
