from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been added to List!")

    all_item = List.objects.all
    return render(request, 'home.html', {'all_item': all_item})


def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item has been deleted from List!")
    return redirect("home")


def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect("home")


def incomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect("home")