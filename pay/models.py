from django.db import models
from uuid import uuid4

class Account(models.Model):
    id = models.CharField(primary_key=True,default=uuid4, max_length=50)
    account_status = models.CharField(max_length=50, blank=True, null=True)
    account_purpose = models.TextField(blank=True, null=True)
    account_description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True,blank=True, null=True)
   
    class Meta:
        db_table = 'account'

class Moviment(models.Model):
    id = models.CharField(primary_key=True,default=uuid4, max_length=50)
    code_movement = models.CharField(max_length=50, blank=True, null=True)
    debit_account_number = models.CharField(max_length=50, blank=True, null=True)
    credit_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_debit_code = models.CharField(max_length=50, blank=True, null=True)
    bank_credit_code = models.CharField(max_length=50, blank=True, null=True)
    amount_movement = models.CharField(max_length=50, blank=True, null=True)
    data_movement = models.DateField(blank=True, null=True)
    data_validate_movement = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    n_cheque = models.CharField(max_length=50, blank=True, null=True)
    rubric = models.CharField(max_length=50, blank=True, null=True)
    responsible_movement = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        
        db_table = 'moviment'
    
class Deposit(models.Model):
    id = models.CharField(primary_key=True,default=uuid4, max_length=50)
    amount_numeric = models.CharField(max_length=50)
    applied_fee = models.CharField(max_length=50)
    deposit_limit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = 'deposit'
