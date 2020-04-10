from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html', {'name':'Mak'})

def add(request):
    val1=request.GET['num1']
    val2=request.GET['num2']
    if (val1== ''):
        val1=0
    if (val2 == ''):
        val2 =0

    res = int(val1)+int(val2)
    return render(request, 'result.html', {'result':res})