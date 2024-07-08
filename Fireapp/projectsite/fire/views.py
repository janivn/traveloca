from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import datetime
from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import TransientHouseLocations, TransientHouse, Owner
from datetime import timedelta
import json
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, render

class HomePageView(ListView):
    model = TransientHouseLocations
    context_object_name = 'home'
    template_name = "home.html"

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


def transient_house_location(request):
    # Fetch all TransientHouseLocations
    transient_house_locations = TransientHouseLocations.objects.all()
    

    # Serialize the necessary fields including TransientHouse details through reverse relationship
    transient_house_json = serialize('json', transient_house_locations, 
                                     fields=('name', 'latitude', 'longitude', 'transienthouse__id'))

    context = {
        'transient_house_json': transient_house_json,
    }

    return render(request, 'transient_house.html', context)

def transient_house_detail(request, transient_house_id):
    transient_house = get_object_or_404(TransientHouse, pk=transient_house_id)
    context = {
        'transient_house': transient_house
    }
    return render(request, 'transient_house_detail.html', context)