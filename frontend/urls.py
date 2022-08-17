from django.urls import path
from .views import AccountView


urlpatterns = [
    path('', AccountView.as_view(), name='my_account'),
]