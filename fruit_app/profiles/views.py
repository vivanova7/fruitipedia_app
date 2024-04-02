from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from fruit_app.profiles.forms import CreateProfileForm
from fruit_app.profiles.models import Profile
from fruit_app.web.views import get_profile
from django.views import generic as views


# Create your views here.
def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "profiles/create-profile.html", context)


class ProfileDetails(views.DetailView):
    template_name = "profiles/details-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context)

    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.object.pk, })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['first_name'].label = 'First Name:'
        form.fields['last_name'].label = 'Last Name:'
        form.fields['profile_picture'].label = 'Image URL:'
        form.fields['age'].label = 'Age:'

        return form

class DeleteProfileView(views.DeleteView):
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()

