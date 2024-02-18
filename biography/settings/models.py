
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Org(models.Model):

    name = models.CharField(max_length=128, default='OrgName')
    logo = models.ImageField(upload_to='org/', default='user/default/org.svg', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Org'
        verbose_name_plural = 'Orgs'

    def __str__(self):
        return f'{self.id} : {self.name}'

class Settings(models.Model):

    #Settings
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    slug  = models.CharField(max_length=64, default='xxxxxxxx')
    image = models.ImageField(upload_to='user/images/', default='user/default/user.svg', blank=True)
    date  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return f'{self.id} : {self.user.username}'

