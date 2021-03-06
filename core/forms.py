from django import forms

from bank.models import BankAccount
from core.models import CSV, Category
from transactions.models import Revenue


class BankAccountCreateForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        exclude = (
            'owner',
        )


class RevenueEditForm(forms.ModelForm):
    class Meta:
        model = Revenue
        exclude = (
            'owner',
        )


class CategoryIncludeForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('owner',)


class CSVImportForm(forms.ModelForm):
    class Meta:
        model = CSV
        exclude = ('owner', 'original_file_name')
