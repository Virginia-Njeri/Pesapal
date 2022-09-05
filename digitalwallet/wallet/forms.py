from ast import Load
from dataclasses import field
from django import forms
from .models import  Account, Currency, Customer, Loan, Notifications, Receipt, Reward, Third_Party, Transaction, Wallet 

class RegisterCustomer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class WalletRegister(forms.ModelForm):
    class Meta:
        model=Wallet


        fields="__all__"

class RegisterAccount(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"


class RegisterReceipt(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"  


class RegisterTransactions(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__" 


class Registercard(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__" 

class RegisterLoan(forms.ModelForm):
    class Meta:
        model = Loan
        fields="__all__" 



class RegisterCurrency(forms.ModelForm):
    class Meta:
        model = Currency
        fields="__all__"  

class RegisterThirdParty(forms.ModelForm):
    class Meta:
        model = Third_Party
        fields="__all__"    


class RegisterNotifications(forms.ModelForm):
    class Meta:
        model = Notifications
        fields="__all__" 


class RegisterReward(forms.ModelForm):
    class Meta:
        model = Reward
        fields="__all__" 
        





              




      
