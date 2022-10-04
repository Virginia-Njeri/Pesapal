from urllib import request
from django.shortcuts import render,redirect
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet

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
    return render(request,"wallet/reward.html",{'form':form}) 
   







def register_customer(request):
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = CustomerRegistrationForm()
    return render(request,"wallet/customer.html", {'form':form} ) 
    

def list_customer(request):
    customers = Customer.objects.all() 
    return render  (request,"wallet/customerList.html",{"customers":customers})                 



def register_currency(request):  
    if request.method=="POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = CurrencyRegistrationForm()
    return render(request,"wallet/currency.html", {'form':form} ) 

def list_currency(request):
    currencys = Currency.objects.all() 
    return render (request,"wallet/currencyList.html",{"currencys":currencys})
     
    

def register_Wallet(request):  
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = WalletRegistrationForm()
    return render(request,"wallet/wallet.html", {'form':form} ) 

def list_wallets(request):
    wallets = Wallet.objects.all() 
    return render  (request,"wallet/walletList.html",{"wallets":wallets})






def register_Account(request):  
    if request.method=="POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = AccountRegistrationForm()
    return render(request,"wallet/account.html", {'form':form} ) 

def list_accounts(request):
    accounts = Account.objects.all() 
    return render  (request,"wallet/accountList.html",{"accounts":accounts})



def register_transaction(request):  
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = TransactionRegistrationForm()
    return render(request,"wallet/transaction.html", {'form':form} ) 

def list_transaction(request):
    transactions = Transaction.objects.all() 
    return render(request,"wallet/transactionsList.html",{"transactions":transactions})







def register_card(request):  
    if request.method=="POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = CardRegistrationForm()
    return render(request,"wallet/card.html", {'form':form} ) 

def list_card(request):
    cards = Card.objects.all() 
    return render(request,"wallet/cardList.html",{"cards":cards})    



def register_thirdparty(request):  
    if request.method=="POST":
        form = Third_PartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = Third_PartyRegistrationForm()
    return render(request,"wallet/thirdparty.html", {'form':form} ) 

def list_thirdparty(request):
    thirdpartys = ThirdParty.objects.all() 
    return render  (request,"wallet/walletList.html",{"thirdparty":thirdpartys})




def register_Notifications(request):  
    if request.method=="POST":
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = NotificationsRegistrationForm()
    return render(request,"wallet/notifications.html", {'form':form} ) 

def list_notifications(request):
    nots = Notifications.objects.all() 
    return render(request,"wallet/notificationsList.html",{"nots":nots})



def register_receipt(request):  
    if request.method=="POST":
        form = RecieptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = RecieptRegistrationForm()
    return render(request,"wallet/receipt.html", {'form':form} ) 

def list_receipt(request):
    receipts = Receipt.objects.all() 
    return render  (request,"wallet/receiptList.html",{"receipts":receipts})





def register_loan(request):  
    if request.method=="POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = LoanRegistrationForm()
    return render(request,"wallet/loan.html", {'form':form} ) 

def list_loan(request):
    loans = Loan.objects.all() 
    return render  (request,"wallet/loanList.html",{"loans":loans})




def register_reward(request):  
    if request.method=="POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = RewardRegistrationForm()
    return render(request,"wallet/reward.html", {'form':form} ) 

def list_reward(request):
    rewards = Reward.objects.all() 
    return render (request,"wallet/rewardList.html",{"rewards":rewards})   







def customer_profile (request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})


def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id = customer.id)
    else:
            form = CustomerRegistrationForm(instance=customer)
            return render(request, "wallet/edit_profile.html", {"form": form})



def wallet_profile(request,id)  :
    wallet=Wallet.objects.get(id=id) 
    return render(request,"wallet_profile.html",{"wallet":wallet})         

def edit_wallet(request,id)  :
    wallet=Wallet.objects.get(id=id)   
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST ,initial=wallet) 
        if form.is_valid():
           form.save()
        return redirect("wallet_profile",id=wallet.id)  
    else:
        form=WalletRegistrationForm(instance=wallet)   
        return render(request,"wallet_profile.html",{"form":form})   

def account_profile (request,id):
    account=Account.objects.get(id=id)  
    return render(request,"account_profile.html",{"account":account})  


def edit_account(request,id) :
    account=Account.objects.get(id=id)  
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
            form=AccountRegistrationForm(instance=account)
            return render(request,"edit_account.html",{"form":form})


def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"card_profile.html",{"card":card})

def edit_card(request,id)  :
    card=Card.objects.get(id=id)  
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
            form=CardRegistrationForm(instance=card)
            return render(request,"edit_card.html",{"form":form})

def transaction_profile(request,id):
    transaction=Card.objects.get(id=id)
    return render(request,"transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id)  :
    transaction=Transaction.objects.get(id=id)  
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
            form=TransactionRegistrationForm(instance=transaction)
            return render(request,"edit_transcation.html",{"form":form})


def receipt_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    return render(request,"receipt_profile.html",{"receipt":receipt})

def edit_receipt(request,id)  :
    receipt=Receipt
    if request.method=="POST":
        form=RecieptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)
    else:
            form=RecieptRegistrationForm(instance=receipt)
            return render(request,"edit_receipt.html",{"form":form})



    
