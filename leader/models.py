from django.db import models


class Leader(models.Model):
          name = models.CharField(max_length=300, verbose_name="Rahbar nomi")
          position  = models.CharField(max_length=200, verbose_name="Lavozimi ")
          tel_num = models.CharField(max_length=20, verbose_name="Telefon nomer")
          faks  = models.CharField(max_length=20, verbose_name="Qoshimcha faks")
          image = models.ImageField(upload_to="leader/", verbose_name="leader rasmi ")
          email   = models.EmailField( verbose_name="Email  nomi")
          reception_time  =  models.CharField(max_length=400, verbose_name="Qabul vaqti ")
          title = models.TextField()

          class Meta:
                    verbose_name = "Rahbar "
                    verbose_name_plural = "Rahbarlar"
                    ordering = ['id']
