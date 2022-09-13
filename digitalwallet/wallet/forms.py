from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model =Wallet
        fields ="__all__"

class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model =Currency
        fields ="__all__"        

class AccountRegistrationForm(forms.ModelForm):
    class Meta:               
        model =Account
        fields ="__all__"        

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model =Transaction
        fields ="__all__"        

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model =Card
        fields ="__all__"        

class Third_PartyRegistrationForm(forms.ModelForm):
    class Meta:
        model =ThirdParty
        fields ="__all__"        

class NotificationsRegistrationForm(forms.ModelForm):
    class Meta:
        model =Notifications
        fields ="__all__"        

class RecieptRegistrationForm(forms.ModelForm):
    class Meta:
        model =Receipt
        fields ="__all__"        

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model =Loan
        fields ="__all__"        

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model =Reward
        fields ="__all__"
              




    
