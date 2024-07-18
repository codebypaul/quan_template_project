from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Models
from app.models import Builder,ChinaParts,Labor,Plan
# Paginator
from django.core.paginator import Paginator

# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World')
    return render(request, 'home.html', context={}, status=200)


# def builders

# estimate form
def estimate_form(request):
    builders = Builder.objects.all().order_by('name')
    context = {
        'builders':builders,
    }
    return render(request,'forms/estimate_form.html',context=context,status=200)

def get_estimate(request):
    # if request.method == 'POST':

    print(request.POST)
    # print(request.POST.get('builder'))
    # print(request.POST.get('project_name'))
    return HttpResponseRedirect("/build_estimate/")

# Pricing List
def pricing_list(request):
    parts_list = ChinaParts.objects.all().order_by('material_type','brand','collection')
    parts_p =Paginator(ChinaParts.objects.all().order_by('material_type','brand','collection'),10)
    parts_page=request.GET.get('parts_page')
    parts=parts_p.get_page(parts_page)

    labor_items=Labor.objects.all().order_by('category','price')
    context={
        'parts_list':parts_list,
        'parts':parts,
        'labor_items':labor_items
    }
    return render(request,'pricing/pricing_list.html',context=context,status=200)

# builder Options
# Builder Profile
def builder_profile(request,builder_id):
    builder=Builder.objects.get(pk=builder_id)

    plan_list=Plan.objects.filter(builder_id=builder_id)
    plan_p=Paginator(Plan.objects.filter(builder_id=builder_id),14)
    plan_page=request.GET.get('plan_page')
    plans = plan_p.get_page(plan_page)

    context={
        'builder':builder,
        'plan_list':plan_list,
        'plans':plans
    }
    return render(request,'builders/profile.html',context=context,status=200)

# Set up new builder
def new_builder(request):
    page_title = 'New Builder'
    context = {
        'builder':''
        }
    return render(request,'forms/new_builder.html',context=context,status=200)

# Edit Builder
def edit_builder(request,builder_id):
    builder = Builder.objects.get(pk=builder_id)
    page_title = builder.name
    context = {
        'builder':builder
        }
    return render(request,'forms/new_builder.html',context=context,status=200)

# view builder information
def view_builders(request):
    builder_list = Builder.objects.all()

    context = {
        'builders':builder_list,
        }
    
    return render(request,'builders/view_builders.html',context=context,status=200)

def new_plan(request):
    context={}
    return render(request,'forms/new_plan.html',context=context,status=200)

def edit_plan(request):
    context={}
    return render(request,'forms/new_plan.html',context=context,status=200)

def view_plan(request,pk):
    plan = Plan.objects.get(pk=pk)
    context={
        'plan':plan
    }
    print(plan)
    return render(request,'builders/plan_info.html',context=context,status=200)

def test(request):
    context={

    }
    return render(request,'test.html',context=context,status=200)