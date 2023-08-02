from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
#function based view returning string as a response

def FBV(request):
    return HttpResponse('<h1>This is function based view ')

#function based view returning html page as a response

def fbv_first(request):
    return render(request,'fbv_first.html')

#Class based view returning a string as a response

class CBV(View):
    def get(self,request):
        return HttpResponse('<h1>This is class based view')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')