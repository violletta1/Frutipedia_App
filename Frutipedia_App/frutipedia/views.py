from django.shortcuts import render, redirect
from Frutipedia_App.frutipedia.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm
from Frutipedia_App.frutipedia.models import ProfileModel,FruitModel
from Frutipedia_App.frutipedia.templatetags.custom_tag import get_profile


# Create your views here.


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = FruitModel.objects.all()
    context = {'fruits': fruits}
    return render(request, 'common/dashboard.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    posts = FruitModel.objects.all().count()
    context = {'posts': posts}
    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = ProfileModel.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')
    return render(request, 'profile/delete-profile.html')


def create_fruit(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {'form': form}
    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request,pk):
    fruit = FruitModel.objects.filter(pk= pk).get()
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)


def fruit_edit(request,pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruits/edit-fruit.html', context)


def fruit_delete(request,pk):
    fruit = FruitModel.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {'form': form, 'fruit': fruit}
    return render(request, 'fruits/delete-fruit.html', context)


