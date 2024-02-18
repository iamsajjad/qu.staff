from datetime import datetime

from django.db import models

# Create your models here.

class Publication(models.Model):

    #Publication
    title            = models.CharField(max_length=1024, default='', blank=True)
    researchers      = models.CharField(max_length=1024, default='', blank=True)
    publication_date = models.DateTimeField(auto_now=False, default=datetime.strptime('1999-01-17', '%Y-%m-%d').date(), blank=True)
    journal          = models.CharField(max_length=1024, default='', blank=True)
    volume           = models.IntegerField(default=0, blank=True)
    issue            = models.IntegerField(default=0, blank=True)
    pages            = models.CharField(max_length=1024, default='', blank=True)
    book             = models.CharField(max_length=1024, default='', blank=True)
    publisher        = models.CharField(max_length=1024, default='', blank=True)
    description      = models.TextField(default='', blank=True)

    url              = models.URLField(max_length=256, db_index=True, unique=True, blank=False)

    date             = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('-publication_date',)
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        return f'{self.id} : {self.title}'

