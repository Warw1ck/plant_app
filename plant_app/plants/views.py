from django.shortcuts import render, redirect

# Create your views here.
from plant_app.common.models import PlantModel
from plant_app.plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm


def plant_create(request):
    form = CreatePlantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plants/create-plant.html', context=context)


def plant_edit(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant details', pk)

    context = {
        'form': form
    }
    return render(request, 'plants/edit-plant.html', context=context)


def plant_delete(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    form = DeletePlantForm(initial=plant.__dict__)

    context= {
        'form': form
    }
    return render(request, 'plants/delete-plant.html', context=context)

def plant_details(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    context = {
        'plant': plant
    }
    return render(request, 'plants/plant-details.html', context=context)
