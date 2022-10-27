from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet, LoanViewSet, NotificationsViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet
from .views import AccountBuyAirtimeView, AccountDepositView, AccountRepayLoanView, AccountRequestLoanView,AccountTransferView, AccountWithdrawView

router = routers.DefaultRouter()
router.register("customers",CustomerViewSet)
router.register("wallet",WalletViewSet)
router.register("card",WalletViewSet)
router.register("transaction",TransactionViewSet)
router.register("loan",LoanViewSet)
router.register("receipt",ReceiptViewSet)
router.register("notifications",NotificationsViewSet)


urlpatterns=[
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("loan/", AccountRequestLoanView.as_view(), name="requestLoan-view"),
    path("payloan/", AccountRepayLoanView.as_view(), name="loanRepay-view"),
    path("airtime/", AccountBuyAirtimeView.as_view(), name="buyAirtime-view"),
    ]

    

    
    