from booking.forms import BookForm
from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib import messages


# booking an appointment
def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You've Successfully Booked an Appointment!")
            id = form.cleaned_data.get('id')
            return redirect('/view')
    else:
        form = BookForm
    return render(request, 'booking/booking.html', {'form': form})
