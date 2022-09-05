from django.shortcuts import render
from .forms import RegisterAccount, RegisterCurrency, RegisterCustomer, RegisterLoan, RegisterNotifications, RegisterReceipt, RegisterReward, RegisterThirdParty, RegisterTransactions, Registercard, WalletRegister

def register_customer(request):
    vargy=RegisterCustomer()
    return render(request,"register_customer.html",{"form":vargy})



def register_account(request):
    vargy=RegisterAccount()
    return render(request,"register_wallet.html",{"form":vargy})


def register_card(request):
    vargy=WalletRegister()
    return render(request,"register_currency.html",{"form":vargy})


def register_currency(request):
    vargy=RegisterAccount()
    return render(request,"register_transaction.html",{"form":vargy})


def register_loan(request):
    vargy=RegisterLoan()
    return render(request,"register_thirdparty.html",{"form":vargy})


def register_notifications(request):
    vargy=RegisterNotifications()
    return render(request,"register_reward.html",{"form":vargy})


def register_receipt(request):
    vargy=RegisterReceipt()
    return render(request,"register_notifications.html",{"form":vargy})

def register_reward(request):
    vargy=RegisterThirdParty()
    return render(request,"register_loan.html",{"form":vargy})


def register_thirdparty(request):
    vargy=RegisterTransactions()
    return render(request,"register_card.html",{"form":vargy})


def register_transaction(request):
    vargy=Registercard()
    return render(request,"register_account.html",{"form":vargy})



def register_card(request):
    vargy=RegisterCurrency()
    return render(request,"register_receipts.html",{"form":vargy})                






    




    
