
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Log(models.Model):

    #Log
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(default='message')
    date    = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return f'{self.id} : {self.user} : {self.message}'

