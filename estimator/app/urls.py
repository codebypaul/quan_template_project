from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello_world),
    path('build_estimate/',views.estimate_form,name="estimate_builder"),
    path('submit_estimate/',views.get_estimate,name="get estimate"),

    # Pricing
    path('pricing_lists',views.pricing_list,name="pricing_lists"),

    # builders
    path('builder_profile/<int:builder_id>',views.builder_profile,name='builder profile'),
    path('add_builder/',views.new_builder,name="add_builder"),
    path('edit_builder/<int:builder_id>',views.edit_builder,name="edit builder"),
    path('builders_list/',views.view_builders,name="view_builders"),
    # plans
    path('new_plan/',views.new_plan,name='add new plan'),
    path('edit_plan/',views.new_plan,name='edit plan'),
    path('view_plan/<int:pk>',views.view_plan,name='view plan'),

    path('test/',views.test,name='test')
]