from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class PhoneBook(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False , db_index=True, verbose_name='Name')
    last_name= models.CharField(max_length=20, null=False, blank=False , db_index=True, verbose_name='Last Name')
    phone = models.CharField(max_length=20, null=False, blank=False , db_index=True, verbose_name='Phone Number')
    address = models.CharField(max_length=200, null=True, blank=True , verbose_name='Address')
    email = models.CharField(max_length=100, null=True, blank=True , verbose_name='Email')
    note = models.CharField(max_length=100, null=True, blank=True , verbose_name='Note')
    creator = models.ForeignKey(User , on_delete=models.PROTECT, verbose_name='Creator')

    class Meta:
        ordering = ['name']
    def __str__(self):
        return str(self.name)  + str(self.last_name)

    def get_absolute_url(self):
        return reverse('phonebook-detail',kwargs={'pk':self.pk})

