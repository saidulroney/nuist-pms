from django.db import models
from datetime import date
from datetime import datetime
from accounts.models import Registration as User
# Create your models here.

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

QUES_CHOICE = (
    ('book', 'What Is your favorite book?'),
    ('food', 'What is your favorite food?'),
    ('city', 'What city were you born in?'),
    ('place', 'Where is your favorite place to vacation?'),
)


CURRENCY = (
    ('USD', 'DOLLAR'),
    ('BDT', 'TAKA'),
    ('CNY', 'YUAN')
)
PLOT_CHOICE = (
    ('two', 'Two Wheeler'),
    ('three', 'Three Wheeler'),
    ('four', 'Four Wheeler'),

)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=200, default="null")
    contactno = models.CharField(max_length=10, default="")
    question = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name


class Complaints(models.Model):
    name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10, default="")
    email = models.EmailField(default="null")
    address = models.CharField(max_length=200, default="")
    complaint_type = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name


class Fare(models.Model):
    per_hour_fare = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY, default='CNY')
    plot_type = models.CharField(
        max_length=10, choices=PLOT_CHOICE, default='four')

    def __str__(self):
        return self.plot_type


class Plots(models.Model):
    floor = models.IntegerField()
    block = models.CharField(max_length=1)
    plot_no = models.IntegerField()
    booked = models.BooleanField(default=False)
    plot_type = models.CharField(
        max_length=10, choices=PLOT_CHOICE, default='four')

    class Meta:
        verbose_name_plural = 'Plots'

    def __str__(self):
        return f'{self.floor } - {self.block} - {self.plot_no}'


class BookedPlots(models.Model):
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    plot_no = models.ForeignKey(Plots, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now=True)
    plot_id = models.IntegerField(default=0)
    is_exited = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Booked Plots'

    def __str__(self):
        return f'{self.plot_no.floor } - { self.plot_no.block} - { self.plot_no.plot_no}'
