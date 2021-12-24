from django import template
from parking.models import BookedPlots,Fare,Plots
from datetime import datetime

register = template.Library()

@register.filter(name = 'adder')
def extention_adder(value):
    value = str(value)

    if value[::-1] == '0':
        return value

    elif value[::-1]== '1':
        return value + 'st'

    elif value[::-1]== '2':
        return value + 'nd'

    elif value[::-1]== '3':
        return value + 'rd'
    
    else:
        return value + 'th'

@register.simple_tag
def my_booked_plots(user):
    # current_user = request.user
    my_booked_plots = BookedPlots.objects.filter(booked_by=user, is_exited=False).count()

    return my_booked_plots

@register.simple_tag
def calculate_fare(user, plot_id, plot_type):
    current_time = datetime.now()
    my_booked_plot = BookedPlots.objects.get(booked_by=user, id=plot_id)
    total_hours = current_time.hour - (my_booked_plot.booking_time.hour + 6)

    #calculate total fare

    fare = Fare.objects.get(plot_type=plot_type)

    total_amount = fare.per_hour_fare * abs(total_hours)
    print(total_amount)


    return total_amount

@register.simple_tag
def total_hours(user, plot_id):
    current_time = datetime.now()
    my_booked_plot = BookedPlots.objects.get(booked_by=user, id=plot_id)
    total_hours = current_time.hour - (my_booked_plot.booking_time.hour + 6)
    return total_hours



@register.simple_tag
def show_price(plot_type):
    plot_price = Fare.objects.filter(plot_type=plot_type).first()
    return plot_price.per_hour_fare

@register.simple_tag
def show_currency(plot_type):
    plot_currency = Fare.objects.filter(plot_type=plot_type).first()
    return plot_currency.currency
    
