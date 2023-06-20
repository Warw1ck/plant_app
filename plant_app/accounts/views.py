from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from plant_app.accounts.forms import CreateProfileForm, EditProfileForm
from plant_app.accounts.models import ProfileModel
from plant_app.common.models import PlantModel


def profile_create(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'accounts/create-profile.html', context=context)


def profile_edit(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk)
    context = {
        'form': form
    }
    return render(request, 'accounts/edit-profile.html', context=context)


def profile_delete(request, pk):
    profile = ProfileModel.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    return render(request, 'accounts/delete-profile.html')


def profile_details(request):
    profile = ProfileModel.objects.all().first()
    plants = PlantModel.objects.all()
    context = {
        'plants': plants,
        'profile': profile
    }
    return render(request, 'accounts/profile-details.html', context=context)
