from django.urls import path

from fruit_app.profiles.views import create_profile, ProfileDetails, edit_profile, DeleteProfileView

urlpatterns = (
    path("create/", create_profile, name="create_profile"),
    path("details/", ProfileDetails.as_view(), name="profile_details"),
    path("edit/", edit_profile, name="profile_edit"),
    path("delete/", DeleteProfileView.as_view(), name="profile_delete"),

)