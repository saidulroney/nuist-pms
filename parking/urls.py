from django.urls import path
from .import views

app_name = 'parking'


urlpatterns = [
    path('all-plots/', views.AllAvailablePlots.as_view(), name='all-plots'),
    path('my-booked-plots/', views.AllBookedPlots.as_view(), name='my-booked-plots'),
    path('confirm-booking/<int:id>/',
         views.confirmbooking, name='confirm-booking'),
    path('confirm-exit/<int:id>/', views.go_to_exit, name='go-to-exit'),
    path('exit/<int:id>/<int:bid>/', views.exit, name='exit'),
]
