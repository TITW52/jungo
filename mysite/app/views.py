from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse

def index(request):
    ads = Advertisement.objects.all()
    context = {'advertisements': ads}
    return render(request, 'app/index.html', context)

def top_sellers(request):
    return render(request, 'app/top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {'form': form}
    return render(request, 'app/advertisement-post.html', context)

# def register(request):
#     return render(request, 'app_auth/register.html')
#
# def login(request):
#     return render(request, 'app_auth/login.html')
#
# def profile(request):
#     return render(request, 'app_auth/profile.html')