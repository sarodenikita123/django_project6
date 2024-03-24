from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("order successfully!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Food.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Food.objects.get(id=pk)
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Food.objects.get(id=pk)
    form = FoodForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)
