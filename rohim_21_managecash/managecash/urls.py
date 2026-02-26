from django.urls import path
from managecash.views import *

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('', login_page, name='login_page'),
    path('dashboard/',dashboard, name='dashboard'),
    path('logout/',logout_function, name='logout_function'),
    path('transactions/', transactions, name='transactions'),

    #---------Cash
    path('cash-list/',cash_list, name='cash_list'),
    path('add-cash/',add_cash, name='add_cash'),
    path('update-cash/<int:pk>/',edit_cash, name='edit_cash'),
    path('delete-cash/<int:pk>/',delete_cash, name='delete_cash'),

    #-------Expense
    path('expense-list/',expense_list, name='expense_list'),
    path('add-expense/',add_expense, name='add_expense'),
    path('update-expense/<int:pk>/',edit_expense, name='edit_expense'),
    path('delete-expense/<int:pk>/',delete_expense, name='delete_expense'),
    
]