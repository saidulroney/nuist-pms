from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import Complaints
from .models import Plots
from .models import BookedPlots
from .models import Fare


class BookedPlotAdmin(admin.ModelAdmin):
    list_display = ['booked_by', 'plot_no', 'plot_id', 'booking_time']


admin.site.register(Contact)
admin.site.register(Complaints)
admin.site.register(Plots)
admin.site.register(Fare)
admin.site.register(BookedPlots, BookedPlotAdmin)
