from django.urls import path
from .views import PaymentAPI


urlpatterns = [
    path('user_payment/', PaymentAPI.as_view(), name='user_payment')
]