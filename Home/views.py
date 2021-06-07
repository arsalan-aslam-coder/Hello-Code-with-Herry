from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("This is Home Page")
    context={
        'var1': "Henil",
        'var2': "Rahul"
    }
    return render(request, "index.html",context)

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")
