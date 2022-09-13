from django.shortcuts import render
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
    customer = Customer.objects.all() 
    return render  (request,"wallet/customerList.html",{"customers":customer})                 



def register_currency(request):  
    if request.method=="POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = CurrencyRegistrationForm()
    return render(request,"wallet/currency.html", {'form':form} ) 

def list_currency(request):
    currency = Currency.objects.all() 
    return render  (request,"wallet/currencyList.html",{"currency":currency})
     
    

def register_Wallet(request):  
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = WalletRegistrationForm()
    return render(request,"wallet/wallet.html", {'form':form} ) 

def list_wallets(request):
    currency = Wallet.objects.all() 
    return render  (request,"wallet/walletList.html",{"currency":currency})






def register_Account(request):  
    if request.method=="POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = AccountRegistrationForm()
    return render(request,"wallet/account.html", {'form':form} ) 

def list_accounts(request):
    currency = Account.objects.all() 
    return render  (request,"wallet/accountList.html",{"currency":currency})



def register_transaction(request):  
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = TransactionRegistrationForm()
    return render(request,"wallet/transaction.html", {'form':form} ) 

def list_transaction(request):
    transaction = Transaction.objects.all() 
    return render (request,"wallet/transactionList.html",{"transaction":transaction})







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
    return render  (request,"wallet/cardList.html",{"cards":cards})    



def register_thirdparty(request):  
    if request.method=="POST":
        form = Third_PartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = Third_PartyRegistrationForm()
    return render(request,"wallet/thirdparty.html", {'form':form} ) 

def list_thirdparty(request):
    thirdparty = ThirdParty.objects.all() 
    return render  (request,"wallet/walletList.html",{"thirdparty":thirdparty})




def register_Notifications(request):  
    if request.method=="POST":
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = NotificationsRegistrationForm()
    return render(request,"wallet/notifications.html", {'form':form} ) 

def list_notifications(request):
    notifications = Notifications.objects.all() 
    return render  (request,"wallet/notificationsList.html",{"notifications":notifications})



def register_receipt(request):  
    if request.method=="POST":
        form = RecieptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = RecieptRegistrationForm()
    return render(request,"wallet/receipt.html", {'form':form} ) 

def list_receipt(request):
    receipt = Receipt.objects.all() 
    return render  (request,"wallet/receiptList.html",{"receipt":receipt})





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
    return render (request,"wallet/rewardList.html",{"reward":rewards})    





    
