from django.shortcuts import render
from .forms import RegisterCustomer

def register_customer(request):
    vargy=RegisterCustomer()
    return render(request,"register_customer.html",{"form":vargy})


    




    
