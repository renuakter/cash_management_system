from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from managecash.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from managecash.forms import *


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        username_exists = AuthUserModel.objects.filter(username=username).exists()
        email_exists = AuthUserModel.objects.filter(email=email).exists()

        if username_exists or email_exists:
            messages.error(request, 'Username or Email already exists.')
            return redirect('register_page')

        if password == conf_password:
            AuthUserModel.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'User Create successfully')
            return redirect('login_page')
        else:
            messages.error(request, 'Both password not match.')
            return redirect('register_page')

    return render(request, 'auth/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_page')
    return render(request, 'auth/login.html')

@login_required
def dashboard(request):
    total_cash = CashModel.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    total_expense = ExpenceModel.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0

    total_balance = total_cash - total_expense

    context = {
        'total_cash':total_cash,
        'total_expense': total_expense,
        'total_balance': total_balance
    }

    return render(request, 'dashboard.html', context)

def logout_function(request):
    logout(request)
    return redirect('login_page')


#-----Cash
def cash_list(request):
    cash_data = CashModel.objects.filter(user=request.user)
    context = {
        'cash_data': cash_data
    }
    return render(request, 'cash/cash-list.html',context)

def add_cash(request):
    if request.method == 'POST':
        cash_form = CashForm(request.POST)
        if cash_form.is_valid():
            cash_data = cash_form.save(commit=False)
            cash_data.user = request.user
            cash_data.save()
            return redirect('cash_list')
    
    cash_form = CashForm()

    context = {
        'cash_form':cash_form, 
        'title': 'Add Cash Info',
        'button': 'Add Cash'
    }

    return render(request, 'cash/cash-form.html', context)

def edit_cash(request, pk):
    cash_data = CashModel.objects.get(id = pk)
    if request.method == 'POST':
        cash_form = CashForm(request.POST, instance=cash_data)
        if cash_form.is_valid():
            cash_data = cash_form.save(commit=False)
            cash_data.user = request.user
            cash_data.save()
            return redirect('cash_list')
    
    cash_form = CashForm(instance=cash_data)

    context = {
        'cash_form':cash_form, 
        'title': 'Update Cash Info',
        'button': 'Update Cash'
    }

    return render(request, 'cash/cash-form.html', context)

def delete_cash(request, pk):
    CashModel.objects.get(id = pk).delete()
    return redirect('cash_list')

#----Expense
def expense_list(request):
    expense_data = ExpenceModel.objects.filter(user = request.user)
    context = {
        'expense_data': expense_data,
    }
    return render(request,'expense/expense-list.html',context)

def add_expense(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_data = expense_form.save(commit=False)
            expense_data.user = request.user
            expense_data.save()
            return redirect('expense_list')
    expense_form = ExpenseForm()

    context = {
        'expense_form':expense_form, 
        'title': 'Add Expense Info',
        'button': 'Add Expense'
    }

    return render(request,'expense/expense-form.html', context)

def edit_expense(request,pk):
    expense_data = ExpenceModel.objects.get(id = pk)
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, instance=expense_data)
        if expense_form.is_valid():
            expense_data = expense_form.save(commit=False)
            expense_data.user = request.user
            expense_data.save()
            return redirect('expense_list')
    expense_form = ExpenseForm(instance=expense_data)

    context = {
        'expense_form':expense_form, 
        'title': 'Update Expense Info',
        'button': 'Update Expense'
    }

    return render(request,'expense/expense-form.html', context)

def delete_expense(request,pk):
    ExpenceModel.objects.get(id = pk).delete()
    return redirect('expense_list')

def transactions(request):
    cash_data = CashModel.objects.filter(user=request.user)
    expense_data = ExpenceModel.objects.filter(user = request.user)

    context = {
        'cash_data': cash_data,
        'expense_data': expense_data
    }
    return render(request,'transaction.html',context)