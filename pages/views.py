from django.shortcuts import render
from django.contrib import messages
from parking.models import Contact, Complaints, BookedPlots
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def complaints(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        contact_no = request.POST.get('contact_no', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', ' null ')
        complaint_type = request.POST.get('complaint_type', ' null ')
        message = request.POST.get('message', ' null ')
        complaint = Complaints(name=name, contact_no=contact_no,
                               email=email, address=address, complaint_type=complaint_type, message=message)
        complaint.save()
        messages.success(
            request, 'Complaint Sent')
    return render(request, 'pages/complaints.html')


def fare(request):
    return render(request, 'pages/fare.html')


def contactus(request):
    if request.method == "POST":
        print('contact')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        contactno = request.POST.get('contactno')
        question = request.POST.get('question')
        contactus = Contact(name=name, mail=mail,
                            contactno=contactno, question=question)
        contactus.save()
        messages.success(
            request, 'Message Sent')
    return render(request, 'pages/contactus.html')


def about(request):
    return render(request, 'pages/aboutus.html')
