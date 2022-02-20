from atexit import register
from django.contrib import admin
from . import models


class TripExpenseInline(admin.TabularInline):
    autocomplete_fields = ['expense']
    model = models.TripExpense

class TripStaffInline(admin.TabularInline):
    autocomplete_fields = ['staff']
    model = models.TripStaff

@admin.register(models.Trip)
class TripAdmin(admin.ModelAdmin):
    inlines = [TripExpenseInline, TripStaffInline]

    list_display = ['start_date', 'end_date', 'income']




@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['staff']



@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
