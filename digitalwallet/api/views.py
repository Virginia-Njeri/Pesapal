
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet
from .serializers import CardSerializer, CustomerSerializer, LoanSerializer, ReceiptSerializer, TransactionSerializer,WalletSerializer
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class =CustomerSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset= Wallet.objects.all()
    serializer_class =WalletSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class =CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class =TransactionSerializer  

class LoanViewSet(viewsets.ModelViewSet):
    queryset= Loan.objects.all()
    serializer_class =LoanSerializer 

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset= Receipt.objects.all()
    serializer_class =Receipt      

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset= Notifications.objects.all()
    serializer_class =Notifications        




