from django.shortcuts import render, HttpResponse, redirect
from . import models


def shows(request):
    context = {
        'shows' : models.get_all_shows()
    }
    return render(request, "shows.html", context)

def new_show(request):
    return render(request, "new.html")

def show_by_id(request, id):
    context = {
        'show'  : models.get_show_by_id(id)
    }
    return render(request, "show-id.html", context)

def edit_show(request, id):
    context = {
        'show'  : models.get_show_by_id(id)
    }
    return render(request, "show-edit.html", context)

def new_show_create(request):
    if request.method == "POST":
        models.create_new_show(request.POST)
        return redirect('/shows')
    else:
        HttpResponse("Something went wrong!")

def delete_show(request, id):
    models.delete_show(id)
    return redirect('/shows')

def update_show(request, id):
    if request.method == "POST":
        models.update_show(request.POST ,id)
        return redirect('/shows/' + str(id))
    else:
        HttpResponse("Something went wrong!")