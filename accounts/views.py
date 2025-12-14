from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                college=form.cleaned_data['college'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                education=form.cleaned_data['education'],
                passout_year=form.cleaned_data['passout_year']
            )
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

