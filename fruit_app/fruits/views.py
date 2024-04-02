from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from fruit_app.fruits.forms import CreateFruitForm
from fruit_app.fruits.models import Fruit
from fruit_app.web.views import get_profile
from django.views import generic as views


# Create your views here.
def add_fruit(request):
    profile = get_profile()
    form = CreateFruitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)

class FruitDetails(views.DetailView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/details-fruit.html'

class FruitUpdate(views.UpdateView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/edit-fruit.html'
    fields = ('fruit_name', 'fruit_image_url', 'description', 'nutrition_info')
    success_url = reverse_lazy('dashboard')

class FruitDelete(views.DeleteView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')
    form_class = modelform_factory(
        Fruit,
        fields=('fruit_name', 'fruit_image_url', 'description', 'nutrition_info'),
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs