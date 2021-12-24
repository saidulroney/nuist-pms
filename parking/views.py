from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db.models.signals import post_save
from .models import Contact, Complaints, Plots, BookedPlots
from accounts.models import Registration
from .forms import PlotBookingForm


class AllAvailablePlots(ListView):
    model = Plots
    template_name = 'all_plots.html'
    context_object_name = 'plots'

    def get_queryset(self):
        return self.model.objects.filter(booked=False)


@login_required
def confirmbooking(request, id):
    obj = Plots.objects.get(id=id)
    obj.save(update_fields=["booked"])

    user = request.user
    url = request.META.get("HTTP_REFERER")  # get last url

    @receiver(post_save, sender=Plots)
    def create_object(sender, instance, created, **kwargs):
        if created and instance.booked == False:
            obj.booked = True
            obj.save()
            # print(instance)
            BookedPlots.objects.create(
                booked_by=user, plot_no=instance, plot_id=instance.id)
            post_save.connect(create_object, sender=Plots)

    create_object(sender=Plots, instance=obj, created=True)
    return redirect(url)


@login_required
def go_to_exit(request, id):
    data = BookedPlots.objects.get(id=id)
    context = {
        'plot': data,
    }
    return render(request, 'confirm_exit.html', context)


@login_required
def exit(request, id, bid):
    obj = Plots.objects.get(id=id)
    obj.booked = False
    obj.save()

    booked_obj = BookedPlots.objects.get(id=bid)
    booked_obj.is_exited = True
    booked_obj.save()
    return redirect('pages:index')


class AllBookedPlots(LoginRequiredMixin, ListView):
    model = BookedPlots
    template_name = 'my_booked_plots.html'
    context_object_name = 'booked_plots'

    def get_queryset(self):
        data = self.model.objects.filter(
            booked_by=self.request.user, is_exited=False)
        print(data)
        return data
