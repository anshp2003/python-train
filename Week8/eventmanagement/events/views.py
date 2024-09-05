from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, Event
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket

@login_required
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event.html', {'events': events})


def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Handle the booking logic here
    return render(request, 'book_ticket.html', {'event': event})

