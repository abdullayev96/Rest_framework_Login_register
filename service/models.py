from django.db import models



class ServiceName(models.Model):
      name = models.CharField(max_length=300, verbose_name="xizmat nomi")
      full_name  = models.CharField(max_length=200, verbose_name="ism")
      title  =  models.TextField()
      position  = models.CharField(max_length=100, verbose_name="Lavozim darajasi")
      image  = models.ImageField(upload_to='ser/')
      email  =  models.EmailField()
      number   = models.CharField(max_length=30, verbose_name="tel nomer")

      class Meta:
            verbose_name = "Xizmat"
            verbose_name_plural = "Xizmatlar"
            ordering = ['id']



