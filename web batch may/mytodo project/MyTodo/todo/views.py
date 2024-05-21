from django.shortcuts import render, redirect
from todo.models import savetodo
# Create your views here.

def homepage(request):
    data = savetodo.objects.all().order_by("-id")
    return render(request, "home.html", {'mytodos' : data})


def savingtodo(request):
    if request.method == "POST":
        todo_title = request.POST.get("title")
        todo_dec = request.POST.get("dec")
        data = savetodo(title = todo_title, desc = todo_dec)
        data.save()

    return redirect("home")