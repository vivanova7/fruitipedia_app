from django.urls import path

from fruit_app.web.views import index, dashboard

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
)