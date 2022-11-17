from django.shortcuts import render

# Create your views here.

def display(request, name):
    #use in view func or pass to template via context
    context = {'name': name}
    return render(request, "main/index.html", context)
