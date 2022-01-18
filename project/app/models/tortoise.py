from enum import auto
from fastapi.applications import FastAPI
from tortoise import fields, models
from tortoise.fields.data import IntField


class Bank(models.Model):
    id = fields.IntField(pk=True)
    Bank_Name = fields.CharField(max_length=50)
    Bank_Masked_Name = fields.CharField(max_length=50)
    Toggle_Display = fields.BooleanField()


class Segment(models.Model):
    id = fields.IntField(pk=True)
    Segment_Name = fields.CharField(max_length=100)
    Toggle_Segment = fields.BooleanField()
    owner= fields.ForeignKeyField('models.Banker', related_name='Segment')


class Banker(models.Model):
    id = fields.IntField(pk=True)
    Bank = fields.CharField(max_length=100)
    Market_Segment = fields.CharField(max_length=100)
    Banker_Name = fields.CharField(max_length=100)
    Banker_Contact_No = fields.BigIntField(digits=10)
    Banker_Email_Address = fields.CharField(max_length=100)
    Remarks = fields.TextField()
    Banker_Start_Date = fields.DateField(auto_now_add=True, null=True)
    Banker_End_Date = fields.DateField(auto_now_add=True, null=True)
    Banker_status = fields.CharField(max_length=20)