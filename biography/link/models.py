
from django.db import models

# Create your models here.

class Link(models.Model):

    #Link
    url  = models.URLField(max_length=256, db_index=True, unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return f'{self.id} : {self.url}'

