from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('fare/', views.fare, name='fare'),
    path('about-us/', views.about, name='aboutus'),
    path('contact-us/', views.contactus, name='contactus'),
    path('complaints/', views.complaints, name='complaints'),
]
