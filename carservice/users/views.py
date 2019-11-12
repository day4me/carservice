from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, InfoForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        info_form = InfoForm(request.POST)
        if form.is_valid() and info_form.is_valid():
            user = form.save()
            info = info_form.save(commit=False)
            info.user = user
            info.save()
            messages.success(request, f'Аккаунт створений, тепер ви можете увійти!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        info_form = InfoForm()
    return render(request, 'users/register.html', {'form': form, 'info_form': info_form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')