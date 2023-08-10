from django.db import models


class IpModel(models.Model):
      ip  = models.CharField(max_length=40)

      def __str__(self):
          return self.ip


class  Category(models.Model):
       name = models.CharField(max_length=300, verbose_name="cat nomi")

       def __str__(self):
           return self.name

class Vacancy(models.Model):
      name = models.CharField(max_length=200, verbose_name="vakansiya yonalishi")
      experience  = models.CharField(max_length=300, verbose_name="Ish tajribasi")
      title = models.TextField()
      cat  = models.ForeignKey(Category, on_delete=models.CASCADE)
      views = models.ManyToManyField(IpModel, related_name="soni", blank=True)
      number  = models.CharField(max_length=50, verbose_name="tel nomer")
      created  = models.DateTimeField(auto_now_add=True)

      def total_views(self):
                return self.views.count()

      def __str__(self):
          return self.name




