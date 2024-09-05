from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from events.models import Ticket,Event
from django.contrib.auth.decorators import login_required

@login_required
def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        ticket_quantity = request.POST.get('ticket_quantity')

        # Create and save the ticket
        Ticket.objects.create(
            event=event,
            username=username,
            contact=contact,
            email=email,
            ticket_quantity=ticket_quantity,
            status='Pending',
            user=request.user  # Assign the logged-in user
        )

        return redirect('index')  # Redirect to the dashboard

    return render(request, 'book_ticket.html', {'event': event})


@user_passes_test(lambda u: u.is_staff)
def approve_ticket(request):
    tickets = Ticket.objects.filter(status='Pending')

    if request.method == 'POST':
        ticket_ids = request.POST.getlist('ticket_ids')
        for ticket_id in ticket_ids:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            ticket.status = 'Approved'
            ticket.save()
        return redirect('approve_ticket')  # Redirect after approval

    return render(request, 'approve_tickets.html', {'tickets': tickets})
