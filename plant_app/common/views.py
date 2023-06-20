from django.shortcuts import render

# Create your views here.
from plant_app.accounts.models import ProfileModel
from plant_app.common.models import PlantModel


def home_page(request):
    profile = ProfileModel.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'common/home-page.html', context=context)


def catalogue_page(request):
    plants = PlantModel.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'common/catalogue.html', context=context)