from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.files.base import ContentFile
from .models import GeeksModel
from .forms import GeeksForm
import markdown2 #mark = markdown2.Markdown()
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def monica(request):
    return HttpResponse ('Hello, Monica!')

def greet (request, name):
    return render (request, "encyclopedia/greet.html", {
        "name": markdown2.markdown(util.get_entry(name)),
        #"name" : name.capitalize()
        #get_entry(name)
    })


def search(request,name):
    return render (request, "encyclopedia/greet.html", {
        "name": markdown2.markdown(util.get_entry(name)),
        #"name" : name.capitalize()
        #get_entry(name)
    })
    #1. Get the string that the user searched from the form.
    #2. Get the list of entries. You can use one of the util functions provided.
    #3. See if the search string is in the list of entries. If yes, return the page of that entry.
    #4. Else, loop over each title in the list of entries and see if the search string is in the individual titles. Create an empty list. If the search string is in any title, append that title into the list. Then return a results page with that list of titles.

def random(request):
    i = random(len(util.list_entries()))
    entries = util.list_entries()
    return render (request, "encyclopedia/greet.html", {
        markdown2.markdown(util.get_entry(entries[i])),
        #"name" : name.capitalize()
        #get_entry(name)
    })

def create (request):
# dictionary for initial data with
    # field names as keys
    context ={}
    #if request.method == "POST":
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        util.save_entry(title,content)
#            return HttpResponseRedirect('encyclopedia/create.html',{'form':form})
    context['form']= form
    return render(request, "encyclopedia/create.html", context)
            #{
            #        "name":title,
            #        "content": content
            #        })
