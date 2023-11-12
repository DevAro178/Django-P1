from django.shortcuts import render, redirect
from django.test import TestCase
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your tests here.
def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "food/index.html", context)


class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item": item}
    return render(request, "food/detail.html", context)


class FoodDetail(DetailView):
    model = Item
    template_name = "food/detail.html"


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    context = {"form": form}
    return render(request, "food/item_form.html", context)


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    context = {"form": form, "item": item}
    return render(request, "food/item_form.html", context)


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    context = {"item": item}
    return render(request, "food/delete_item.html", context)
