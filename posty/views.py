from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from posty.models import Profile
from .forms import ProfileCreateForm

# Create your views here.
@login_required
def home(request):
    """Home page of the application"""

    return render(request,'posty/base.html')

def register(request):
    """Register users to the database"""
    if request.method != 'POST':
        form = ProfileCreateForm()

    else:
        form = ProfileCreateForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()

            Profile.objects.create(user=new_user)
            return redirect('posty:home')

        else:
            return redirect('posty:register')
            
    return render(request,'users/register.html',{'form':form})