from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileCreateForm, ProfileEditForm, UserCreateForm, UserEditForm

# Create your views here.


def register(request):
    """Register users to the database"""
    if request.method != 'POST':
        form = ProfileCreateForm()
        user = UserCreateForm()

    else:
        form = ProfileCreateForm(data=request.POST, files=request.FILES)
        user = UserCreateForm(data=request.POST)

        if form.is_valid() and user.is_valid():
            cd = user.cleaned_data
            new_user = user.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()

            # Profile.objects.create(user=new_user)
            new_profile = form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return redirect('posty:home')

        else:
            return redirect('posty:register')

    return render(request, 'users/register.html', {'form': user, 'profile': form})


@login_required
def edit_profile(request, user_id):
    """Enable users to edit their profiles"""
    # user = User.objects.get(id=user_id)
    # user = get_object_or_404(User,id=user_id)

    if request.method != 'POST':
        profile_edit_form = ProfileEditForm(instance=request.user)
        user_edit_form = UserEditForm(instance=request.user)

    else:
        profile_edit_form = ProfileEditForm(
            data=request.POST, instance=request.user.user_profile, files=request.FILES)
        user_edit_form = UserEditForm(data=request.POST, instance=request.user)

        form_validity = profile_edit_form.is_valid() and user_edit_form.is_valid()
        print(form_validity)
        print(request.FILES)

        if form_validity:
            profile_edit_form.save()
            user_edit_form.save()
            return redirect('posty:home')

        else:
            return redirect('posty:edit_profile', user_id=user_id)

    return render(request, 'users/edit_profile.html', {'form': user_edit_form, 'profile': profile_edit_form})
