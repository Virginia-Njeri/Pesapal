

from django.urls import path 
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_accounts, list_card, list_currency, list_customer, list_loan, list_notifications, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallets, receipt_profile, register_account, register_card, register_currency, register_loan, register_notifications, register_reciept, register_reward, register_third_party, register_transaction, register_wallet, register_customer, transaction_profile, wallet_profile

urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("currency/",register_currency,name="registration"),
    path("account/",register_account,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("card/",register_card,name="registration"),
    path("third_party/",register_third_party,name="registration"),
    path("notifications/",register_notifications,name="registration"),
    path("reciept/",register_reciept,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("reward/",register_reward,name="registration"),

    path("customers/",list_customer,name= "customerList"),
    path("currencies/",list_currency,name="currency"),
    path("wallets/",list_wallets,name="listwallets"),
    path("accounts/",list_accounts,name ="list_accounts"),
    path("transactions/",list_transaction,name="transactions"),
    path("cards/",list_card,name="cards"),
    path("thirdpartys/",list_thirdparty,name="thirdpartys"),
    path("notificationss/",list_notifications,name="notifications"),
    path("receipts/",list_receipt,name="receipts"),
    path("loans/",list_loan,name= "loans"),
    path("rewards/",list_reward,name="reward"),

    
    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("profile/edit/<int:id>/",edit_profile,name="profile"),
    path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/",edit_card,name="edit_account"),
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),
    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),

]









