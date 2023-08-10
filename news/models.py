from django.db import models



class IpModel(models.Model):
          ip =  models.CharField(max_length=100)

          def __str__(self):
              return self.ip


class ImageNews(models.Model):
      image =  models.ImageField(upload_to='bignew/')

      class Meta:
            verbose_name = "Rasmlar"



class News(models.Model):
          name  = models.CharField(max_length=200, verbose_name="nomi")
          image_one  = models.ImageField(upload_to='good/')
          images = models.ManyToManyField(ImageNews, related_name="img", blank=True)
          body  = models.TextField()
          views  = models.ManyToManyField(IpModel, related_name="soni", blank=True)
          created = models.DateTimeField(auto_now_add=True)

          def __str__(self):
              return self.name


          def total_views(self):
              return self.views.count()

          class Meta:
                verbose_name = "yangilik"
                verbose_name_plural = "Yangilikla"
                ordering = ['id']


class BigNewsBaby(models.Model):
      name  = models.CharField(max_length=200, editable=False)
      image = models.ImageField(upload_to='baby/')
      body   = models.TextField()
      address  = models.CharField(max_length=200, editable=True)
      number  =  models.CharField(max_length=40,editable=True)
      leader_name = models.CharField(max_length=200, editable=True)


      def __str__(self):
          return self.name

      class Meta:
            verbose_name = "Single page"
