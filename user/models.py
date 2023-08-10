from django.db import models
from django.core.exceptions import ValidationError
import os
from datetime import datetime

from pathlib import Path
from django.core.files import File
from django.core.files.base import ContentFile






def validate_number(value):
    if value:
            if value>100000:
                raise ValidationError("The number of team per pool is <100000. Please try again.")
    return value



def validate_geeks_mail(value):
          if "@gmail.com"  in value:
                    return value
          else:
                    raise ValidationError("This field accepts mail id of google only")

def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .pdf, .doc, .docx file ')




class SendUser(models.Model):
          NEW = "new"
          EXECUTION = "execution"
          COMPLETED = "completed"
          STATUS_CHOICES = (
                    (NEW, 'new'),
                    (EXECUTION, 'execution'),
                    (COMPLETED, 'completed'),
          )

          reference_number  = models.SmallIntegerField(validators=[validate_number])
          verification_code  = models.CharField(max_length=10)
          full_name   =  models.CharField(max_length=400, verbose_name="Toliq ism Familiya")
          number = models.CharField(max_length=20, verbose_name="Telifon nomeri")
          email   = models.EmailField(validators=[validate_geeks_mail], verbose_name="Email manzili")
          address  = models.CharField(max_length=200, verbose_name="Manzil")
          body  = models.TextField()
          status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="new")
          file  = models.FileField(upload_to="new/",validators=[validate_file])
          created  = models.DateTimeField(auto_now_add=True)



          def __str__(self):
                    return f"{self.id}||{self.full_name} ||  {self.email}"


          class Meta:
                    verbose_name = "Xabar"
                    verbose_name_plural = "Xabarlar"
                    ordering = ['id']

