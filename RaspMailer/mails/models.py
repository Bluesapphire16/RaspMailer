from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

class Folder(models.Model):
    root = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    user_readonly = models.BooleanField()
    group_readonly = models.BooleanField()

class Contact(models.Model):
    email_address = models.EmailField(primary_key=True)
    firstname = models.CharField(max_length=255, default="", blank=True)
    lastname = models.CharField(max_length=255, default="", blank=True)
    referenced_users = models.ManyToManyField(User)

class Mail(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    mail_from = models.ManyToManyField(Contact, related_name="from_relations")
    to = models.ManyToManyField(Contact, related_name="to_relations")
    cc = models.ManyToManyField(Contact, related_name="cc_relations", blank=True)
    bcc = models.ManyToManyField(Contact, related_name="bcc_relations", blank=True)
    subject = models.CharField(max_length=255, default="", blank=True)
    payload = models.TextField(default="", blank=True)
    recivedate = models.DateTimeField();
    originfile = models.CharField(max_length=255, null=True, blank=True)
    mailtype = models.CharField(max_length=32, choices=(
        ("MIME", "MIME"), ("AES_ENCRYPTED", "AES encrypted"), ("RSA_ENCRYPTED", "RSA encrypted")
    ), default="MIME")

admin.site.register(Mail)
admin.site.register(Contact)
admin.site.register(Folder)
