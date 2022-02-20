import datetime
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50, null=True, blank=True)
    id_card = models.CharField(max_length=7)
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    class Meta: 
        ordering = ['name']


class Trip(models.Model):
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    last_updated = models.DateField(auto_now=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'{self.start_date} {self.end_date} {self.income}'
    
    class Meta: 
        ordering = ['start_date']


class TripStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    trp = models.ForeignKey(Trip, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment1 = models.DecimalField(max_digits=10, decimal_places=2)
    payment2 = models.DecimalField(max_digits=10, decimal_places=2)
    payment3 = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)


class Expense(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        ordering = ['title']


class TripExpense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
    expense = models.ForeignKey(Expense, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

