
from rest_framework import serializers


from pyexpat import model
from rest_framework import serializers
from wallet.models import Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","last_name")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=("balance","customer_id")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=("card_number","card_type")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=("transaction_code","wallet")  


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=("loan_id","loan_type","amount","datetime","Wallet") 

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=("receipt_type","receipt_date","bill_number","total_amount","transaction")  

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields=("transaction","transaction_id","customer_id","status")  


        


    





      








      

        
