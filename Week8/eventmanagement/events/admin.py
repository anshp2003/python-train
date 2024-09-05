from django.contrib import admin
from .models import Event
from .models import  Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'price')  # Add 'price' here
    search_fields = ('name', 'location')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('username', 'event', 'ticket_quantity', 'status')
    list_filter = ('status', 'event')
    search_fields = ('username', 'email')


admin.site.register(Ticket, TicketAdmin)
