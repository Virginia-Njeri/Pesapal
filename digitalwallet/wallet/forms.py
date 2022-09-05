from django import forms
from .models import  Customer, Wallet 

class RegisterCustomer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

# class WalletRegister(forms.ModelForm):
#     class Meta:
#         model=Wallet


#         fields="__all__"

# class RegisterAccount(forms.ModelForm):
#     class Meta:
#         model=Account
#         fields="__all__"


# class RegisterReceipt(forms.ModelForm):
#     class Meta:
#         model=Receipt
#         fields="__all__"  


# class RegisterTransactions(forms.ModelForm):
#     class Meta:
#         model=Transaction
#         fields="__all__" 


# class Registercard(forms.ModelForm):
#     class Meta:
#         model=Account
#         fields="__all__"         




      
