from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm,UserUpdateForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Congratulation! A new user {username} has been added')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES,
                                    instance = request.user.profile)
        u_form = UserUpdateForm(request.POST,
                                instance = request.user)
        if u_form.is_valid() :#and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request,f'Congratulation! Profile has been updated')
            return redirect('profile')
    if request.method == 'GET':
        p_form = ProfileUpdateForm( instance = request.user )
        u_form = UserUpdateForm( instance = request.user.profile )
        context = {
            'p_form':p_form,
            'u_form':u_form
        }
    return render(request,'users/profile.html', context)
    



