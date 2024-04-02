from django.urls import path

from fruit_app.fruits.views import add_fruit, FruitDetails, FruitUpdate, FruitDelete

urlpatterns = (
    path('create/', add_fruit, name="add_fruit"),
    path('<int:pk>/details/', FruitDetails.as_view(), name="fruit_details"),
    path('<int:pk>/edit/', FruitUpdate.as_view(), name="fruit_edit"),
    path('<int:pk>/delete/', FruitDelete.as_view(), name="fruit_delete"),

)