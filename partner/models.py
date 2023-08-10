from django.db import models



class Partners(models.Model):
          name = models.CharField(max_length=200, verbose_name="Nomi")
          body = models.TextField()
          image  = models.ImageField(upload_to='hamkorlar/', verbose_name="Hamkorlar rasmi")
          email  = models.EmailField()
          number = models.CharField(max_length=30, verbose_name="Telefon nomer")
          url_name  = models.CharField(max_length=4000, verbose_name="Web sayt silkasi")


          def __str__(self):
                    return self.name

          class Meta:
                    verbose_name = "Hamkor"
                    verbose_name_plural = "Hamkorlar"
                    ordering = ['id']

