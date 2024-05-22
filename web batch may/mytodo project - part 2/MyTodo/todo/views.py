from django.shortcuts import render, redirect
from todo.models import savetodo
from django.http import HttpResponse
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

def deltetodo(request, myid):

    mytodo = savetodo.objects.get(id = myid)
    mytodo.delete()

    return redirect("home")

    # return HttpResponse("data delted")

def updatingttodo(request, todoid):
    mytodo = savetodo.objects.get(id = todoid)
    data = savetodo.objects.all().order_by("-id")
    return render(request, "updatetodo.html", {"todo" : mytodo, 'mytodos' : data})


def updatingthisttodo(request, todoid):
    mytodo = savetodo.objects.get(id = todoid)
    if request.method == "POST":
        todo_title = request.POST.get("title")
        todo_dec = request.POST.get("dec")

        mytodo.title = todo_title
        mytodo.desc = todo_dec
        mytodo.save()

    return redirect("home")