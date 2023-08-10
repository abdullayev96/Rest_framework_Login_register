from django.db import models
import os
from django.core.exceptions import ValidationError



def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', 'excel']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .pdf, .doc, .docx, .excel  file ')

class Information(models.Model):
      name  = models.CharField(max_length=1000, verbose_name="Nomi")
      file  = models.FileField(upload_to='infor/', validators=[validate_file])


      def __str__(self):
          return self.name


