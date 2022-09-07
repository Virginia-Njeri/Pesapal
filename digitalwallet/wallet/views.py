from django.shortcuts import render

from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, RecieptRegistrationForm, RewardRegistrationForm, Third_PartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm



def register_customer(request):
    form=CustomerRegistrationForm()
    return render (request,"wallet/customer.html",
    {'form':form})

def register_currency(request):
    form=CurrencyRegistrationForm()
    return render(request,"wallet/currency.html",
    {'form':form})

def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet/wallet.html",
    {'form':form})  

def register_account(request):
    form=AccountRegistrationForm()
    return render(request,"wallet/account.html",
    {'form':form}) 

def register_transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"wallet/transaction.html",
    {'form':form}) 

def register_notifications(request):
    form=NotificationsRegistrationForm()
    return render(request,"wallet/notifications.html",
    {'form':form})  

def register_card(request):
    form=CardRegistrationForm()
    return render(request,"wallet/card.html",
    {'form':form})

def register_third_party(request):
    form=Third_PartyRegistrationForm()
    return render(request,"wallet/thirdparty.html",
    {'form':form})  

def register_reciept(request):
    form=RecieptRegistrationForm()
    return render(request,"wallet/receipt.html",
    {'form':form})  

def register_loan(request):
    form=LoanRegistrationForm()
    return render(request,"wallet/loan.html",
    {'form':form})  

def register_reward(request):
    form=RewardRegistrationForm()
    return render(request,"wallet/reward.html")
    




    
