from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("This is Home Page")
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")
