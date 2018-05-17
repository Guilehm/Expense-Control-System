from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from core.forms import BankAccountCreateForm
from bank.models import BankAccount
from transactions.models import Expense, Revenue
from transactions.forms import ExpenseForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        accounts = BankAccount.objects.filter(owner=request.user)
        expenses = Expense.objects.filter(user=request.user)
        revenues = Revenue.objects.filter(user=request.user)
        return render(request, 'core/index.html', {
            'accounts': accounts,
            'expenses': expenses,
            'revenues': revenues,
        })
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            messages.add_message(request, messages.SUCCESS, 'Olá, {}, seu login foi efetuado com sucesso'.format(request.user))
            return redirect('core:index')
        else:
            return render(request, 'core/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'login_form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('core:index')
        else:
            if form.errors:
                return render(request,'core/register.html', context)
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'core/register.html', context)

def expenses_include(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('core:index')
        else:
            return render(request, 'core/expenses_include.html', {
                'form': form,
            })
    else:
        form = ExpenseForm()
        return render(request, 'core/expenses_include.html', {
            'form': form,
        })

def bank_accounts_create(request):
    if request.method == 'POST':
        form = BankAccountCreateForm(request.POST)
        if form.is_valid():
            bank_account = form.save(commit=False)
            bank_account.owner = request.user
            bank_account.save()
            messages.add_message(request, messages.SUCCESS, 'Parabéns, sua conta foi criada com sucesso!'.format(request.user))
            return redirect('core:index')
        else:
            return render(request, 'core/bank_accounts_create.html', {
                'form': form,
            })
    else:
        form = BankAccountCreateForm()
        return render(request, 'core/bank_accounts_create.html', {
            'form': form,
        })
