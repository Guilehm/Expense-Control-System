from django.contrib import admin
from transactions.models import Revenue, Expense

# Register your models here.
class RevenueTagInline(admin.StackedInline):
    model = Revenue.tags.through
    extra = 0

@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ['title', 'total', 'category', 'received_out',]
    list_filter = ['title', 'category', 'received_out',]
    exclude = (
        ['tags',]
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    inlines = [
        RevenueTagInline,
    ]


# Register your models here.
class ExpenseTagInline(admin.StackedInline):
    model = Expense.tags.through
    extra = 0

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'total', 'category', 'paid_out',]
    list_filter = ['title', 'category', 'paid_out',]
    exclude = (
        ['tags',]
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    inlines = [
        ExpenseTagInline,
    ]