# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TransactionMethod(models.Model):
        name = models.CharField(max_length=255, unique=True)
        description = models.CharField(max_length=255)

        def __str__(self):
                return self.name

class Thirdparty(models.Model):
        name = models.CharField(max_length=255, unique=True)
        description = models.CharField(max_length=255)

        def __str__(self):
                return self.name

class Transaction(models.Model):
        transaction_date = models.DateTimeField('date of transaction')
        payer = models.ForeignKey(Thirdparty, related_name='payer')
        payee = models.ForeignKey(Thirdparty, related_name='payee')
        amount = models.DecimalField(max_digits=23, decimal_places =2, default=0)
        method = models.ForeignKey(TransactionMethod, null=True, blank=True)

        def __str__(self):
                return self.payer + ":" + self.payee + ":" + self.amount + ":" + self.transaction_date


class Statement(models.Model):
        name = models.ForeignKey(Thirdparty)
        entry_date = models.DateTimeField('date of entry')
	interval_date = models.DateTimeField('interval')
        previous_entry = models.ForeignKey('self', related_name='prev', null=True, blank=True)
        previous_amount = models.DecimalField(max_digits=23, decimal_places =2, default=0)
        income = models.DecimalField(max_digits=23, decimal_places =2, default=0)
        expense = models.DecimalField(max_digits=23, decimal_places =2, default=0)
        net = models.DecimalField(max_digits=23, decimal_places =2, default=0)
	next_entry = models.ForeignKey('self', related_name='next', null=True, blank=True)
	next_amount = models.DecimalField(max_digits=23, decimal_places =2, default=0)
	manual_entry = models.DecimalField(max_digits=23, decimal_places =2, default=0)
	
class Account(models.Model):
	name = models.ForeignKey(Thirdparty)
	default_rate = models.DecimalField(max_digits=5, decimal_places =2, default=0)

class Rate(models.Model):
        name = models.ForeignKey(Thirdparty)
        date_starts = models.DateTimeField('start date of rate')
        date_ends = models.DateTimeField('end date of rate')
        rate = models.DecimalField(max_digits=5, decimal_places =2, default=0)
        accounts = models.ForeignKey(Account)

