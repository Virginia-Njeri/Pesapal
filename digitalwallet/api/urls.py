from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet, LoanViewSet, NotificationsViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet
router = routers.DefaultRouter()
router.register("customers",CustomerViewSet)
router.register("wallet",WalletViewSet)
router.register("card",WalletViewSet)
router.register("transaction",TransactionViewSet)
router.register("loan",LoanViewSet)
router.register("receipt",ReceiptViewSet)
router.register("notifications",NotificationsViewSet)










urlpatterns=[
    path("",include(router.urls)),]