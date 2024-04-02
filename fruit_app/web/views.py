from django.shortcuts import render

from fruit_app.fruits.models import Fruit
from fruit_app.profiles.models import Profile

def get_all_fruits():
    return Fruit.objects.all() if Fruit.objects.all() else None

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def get_profile():
    return Profile.objects.first()

def dashboard(request):
    profile = get_profile()
    fruits = get_all_fruits()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard/dashboard.html', context)