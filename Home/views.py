from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
    #return HttpResponse("This is Home Page")
    context={
        'var1': "Henil",
        'var2': "Rahul"
    }
    return render(request, "index.html",context)

def about(request):
    return render(request, "about.html")

def services(request):
    return HttpResponse("This is Service Page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        date=datetime.today()
        contact=Contact(name=name, email=email, phone=phone,desc=desc,date=date)
        contact.save()
    return render(request, "contact.html")
