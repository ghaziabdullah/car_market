from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.

def AdsListView(request):
    Ads=Car.objects.all()
    return render (request, 'carSelling/ads_list.html', {'Ads':Ads})

def AdDetailView(request, car_id):
    car=Car.objects.get(id=car_id)
    return render (request, 'carSelling/ad_details.html', {'car':car})

def AdDeleteView(request):
    pass

@login_required(login_url='accounts:login')
def NewAdView(request):

    profile_formset= formset_factory(AdForm, extra=1)

    if request.method == 'POST':
        formset = profile_formset(request.POST, request.FILES)
        
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()

            return redirect ('carSelling:ads_list')
    else:
        formset = profile_formset()
    
    return render (request, 'carSelling/new_ad.html', {'formset':formset})