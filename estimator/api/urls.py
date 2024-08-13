from django.urls import path, include
from . import views

urlpatterns = [
    path('builders/',views.builder_list,name='builder list api'),
    path('add_builder/',views.add_builder,name='add builder')
]