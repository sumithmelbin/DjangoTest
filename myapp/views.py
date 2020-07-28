from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from myapp.form import StuForm


def hello(request):
        return HttpResponse("<h2>Hello Welcome to django......Hi sumith</h2>")

def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

def methodinfo(request):
    return HttpResponse("Http request is: "+request.method)

def studentdemo(request):
    if request.method == "POST":
        form = StuForm(request.POST)
        if form.is_valid():
            try:
              return redirect('/')
            except:
                pass
    else:
        stu = StuForm()
    return render(request,"studentdemo.html",{'form':stu})