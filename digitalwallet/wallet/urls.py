from django.urls import path

from .views import register_Account, register_account, register_card, register_currency, register_customer, register_loan, register_notifications, register_receipt, register_reward, register_thirdparty, register_transaction

urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("register/",register_account,name="registration"),
    path("register/",register_card,name="registration"),
    path("register/",register_currency,name="registration"),
    path("register/",register_loan,name="registration"),
    path("register/",register_notifications,name="registration"),
    path("register/",register_receipt,name="registration"),
    path("register/",register_reward,name="registration"),
    path("register/",register_thirdparty,name="registration"),
    path("register/",register_transaction,name="registration"),
    path("register/",register_reward,name="registration"),
    








]