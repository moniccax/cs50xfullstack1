from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import markdown2
from .forms import ProductModelForm
from .models import Product

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        #return HttpResponse('Hello World would be like this')
    })

def monica(request):
    return HttpResponse ('Hello, Monica!')

def greet (request, name):
    return HttpResponse ('Hello, {name}!')


class NewForm(forms.Form):
    title = forms.CharField(label="New View"),
    content = forms.CharField(label="New Content View")
 #.decode("utf-8")commerce
    util.save_entry (title, "teste")


def create(request):

    #form = ProductModelForm()
    #util.form()
    #util.save_entry ("teste", "teste")
    #util.save_entry(form, )
    #    printf ('Printing POST':, request.POST)
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = ProductModelForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data["title"]

            # Add the new task to our list of tasks
            title.append(title)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("wiki:index"))

        else:

            return render(request, "encyclopedia/create.html", {
                "form": ProductModelForm()
    })

def random(request):
    return render(request, "encyclopedia/random.html", {
        "entries": util.get_entry()
    })

def getmark(request):
    mark = markdown2.Markdown()
    mark.convert(entry)
    """
    Convert given markdown to html.
    :param md: string
    :return: string - converted html
    """
    return render(request, "encyclopedia/random.html", {
        util.get_entry()
    })
