import os
from datetime import datetime
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User

from link.models import Link
from publication.models import Publication

# Create your models here.

class Bio(models.Model):

    #Bio
    owner          = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name      = models.CharField(max_length=256, default='', blank=False)
    surname        = models.CharField(max_length=256, default='', blank=True)
    image          = models.ImageField(upload_to='user/images/', default='user/default/user.svg', blank=True)
    birthday       = models.DateTimeField(auto_now=False, default=datetime.strptime('1999-01-17', '%Y-%m-%d').date(), blank=True)
    nationality    = models.CharField(max_length=128, default='', blank=True)
    gender         = models.CharField(max_length=32, default='', blank=True)
    degree         = models.CharField(max_length=32, default='', blank=True)
    academic_title = models.CharField(max_length=256, default='', blank=True)
    college        = models.CharField(max_length=256, default='', blank=True)
    department     = models.CharField(max_length=256, default='', blank=True)
    major          = models.CharField(max_length=256, default='', blank=True)
    specialty      = models.CharField(max_length=256, default='', blank=True)
    position       = models.CharField(max_length=256, default='', blank=True)
    occupation     = models.CharField(max_length=256, default='', blank=True)
    mother_lang    = models.CharField(max_length=256, default='', blank=True)
    other_langs    = models.CharField(max_length=256, default='', blank=True)
    personal_email = models.EmailField(max_length=254, blank=True)
    work_email     = models.EmailField(max_length=254, blank=True)
    create_date    = models.DateTimeField(auto_now_add=True)
    update_date    = models.DateTimeField(auto_now=True)

    # arabic fields
    ar_full_name      = models.CharField(max_length=256, default='', blank=True)
    ar_nationality    = models.CharField(max_length=128, default='', blank=True)
    ar_academic_title = models.CharField(max_length=256, default='', blank=True)
    ar_college        = models.CharField(max_length=256, default='', blank=True)
    ar_department     = models.CharField(max_length=256, default='', blank=True)
    ar_major          = models.CharField(max_length=256, default='', blank=True)
    ar_specialty      = models.CharField(max_length=256, default='', blank=True)
    ar_position       = models.CharField(max_length=256, default='', blank=True)
    ar_occupation     = models.CharField(max_length=256, default='', blank=True)
    ar_mother_lang    = models.CharField(max_length=256, default='', blank=True)
    ar_other_langs    = models.CharField(max_length=256, default='', blank=True)
    ar_state          = models.CharField(max_length=256, default='', blank=True)
    ar_district       = models.CharField(max_length=256, default='', blank=True)
    ar_hiring_date    = models.DateTimeField(default=timezone.now)
    ar_direct_date    = models.DateTimeField(default=timezone.now)

    slug  = models.CharField(max_length=64, default='xxxxxxxx')

    publications      = models.ManyToManyField(Publication, related_name='publications', blank=True)
    links             = models.ManyToManyField(Link, related_name='links', blank=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'Bio'
        verbose_name_plural = 'Bios'

    def __str__(self):
        return f'{self.id} : {self.owner.username}'


@receiver(models.signals.pre_save, sender=Bio)
def change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Bio.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        except Bio.DoesNotExist:
            pass

@receiver(models.signals.post_delete, sender=Bio)
def delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

