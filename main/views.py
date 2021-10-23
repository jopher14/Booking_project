from django.shortcuts import render
from booking.models import BookModel
from .forms import bookForms
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def view(request):
    result = BookModel.objects.all()
    return render(request, 'main/view.html', {'result': result})


def editbook(request, id):
    id = BookModel.objects.get(id=id)
    return render(request, "main/editbook.html", {"result": id})


def updatebook(request, id):
    updatebook = BookModel.objects.get(id=id)
    form = bookForms(request.POST, instance=updatebook)
    if form.is_valid():
        form.save()
        messages.success(
            request, "Your Appointment has been Updated Successfully..!")
        return render(request, "main/editbook.html", {"result": updatebook})
    else:
        return render(request, 'main/editbook.html', {"result": id})
