from .forms import SignupForm, SignupForm2
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def index(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        form_birth = SignupForm2(request.POST)
        # create a new user.
        if form.is_valid() and form_birth.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user_birth = form_birth.save(commit=False)
            new_user_birth.user = new_user
            new_user_birth.save()
            new_user.is_active = True
            login(request, new_user)
            return redirect('signup:success')
        else:
            # handle invalid password
            context = {
                'form': form,
                'form_birth': form_birth
            }
            return render(request, 'signup/index.html', context)
    else:
        form = SignupForm()
        form_birth = SignupForm2()

        context = {
            'form': form,
            'form_birth': form_birth
        }
        return render(request, 'signup/index.html', context)

def success(request):
	return render(request, 'signup/success.html')
