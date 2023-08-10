from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AvtoCategory(models.Model):
          name = models.CharField(max_length=50, verbose_name="Avtobus yili")

          def __str__(self):
              return self.name




class AvtobusYear(models.Model):
          cat  = models.ForeignKey(AvtoCategory, on_delete=models.CASCADE)
          name =  models.CharField(max_length=300, verbose_name="Avtobus nomi ")
          title = models.CharField(max_length=50)
          born_year  = models.CharField(max_length=200, verbose_name="Chiqish yili")
          size   =  models.CharField(max_length=100, verbose_name="odamlarni sigdira oladigan hajmi ")
          seat_count  = models.CharField(max_length=100, verbose_name="Orindiq soni")
          number_direction = models.CharField(max_length=150, verbose_name="Yonalishlar soni ")
          image  = models.ImageField(upload_to='avtobus/')
          content = RichTextUploadingField()


          def __str__(self):
              return self.name

          class Meta:
                verbose_name = "Avtobus haqida"
                ordering = ['id']


class AvtobusBackground(models.Model):
          number = models.CharField(max_length=50, verbose_name="Avtobus raqami")
          direction  =  models.CharField(max_length=40, verbose_name="Yonalishi nomi")
          startend  = models.CharField(max_length=500, verbose_name="Yonalish vaqti ")
          sideways_time  = models.FloatField(verbose_name="Yonalish davomligigi")
          route_length = models.CharField(max_length=300, verbose_name="Yonalish uzunligi")
          bus_brand =  models.CharField(max_length=200, verbose_name="Avtobus markasi ")
          place  = models.CharField(max_length=300, verbose_name="Qoyish joyi")

          class Meta:
                    verbose_name = "Avtobus vaqti"
                    verbose_name_plural = "Avtobuslar vaqtilari"
                    ordering = ['id']



class AvtobusData(models.Model):
          avto_number = models.IntegerField()
          start_place = models.CharField(max_length=200, verbose_name="Boshlangich bekat")
          end_place = models.CharField(max_length=200, verbose_name="Oxirgi  bekat")
          fast_time = models.CharField(max_length=200, verbose_name="Harakat vaqti")


          class Meta:
                verbose_name = "Avtobus malumotlar"
                verbose_name_plural = "Avtobuslar malumotlari "
                ordering = ['id']



class ModelCategory(models.Model):
      name = models.CharField(max_length=400)

      def __str__(self):
          return self.name

class BusImage(models.Model):
      image = models.ImageField(upload_to='bus/')



class BusOrder(models.Model):
      cat  = models.ForeignKey(ModelCategory, on_delete=models.CASCADE)
      size = models.CharField(max_length=100, verbose_name="Odamlar sigdira oladigan  hajmi")
      price = models.IntegerField()
      images =  models.ManyToManyField(BusImage, related_name="rasmlar", blank=True)



      def __str__(self):
          return self.size


class RegionName(models.Model):
      name  = models.CharField(max_length=100)


      def __str__(self):
          return self.name


class OrderPost(models.Model):
      full_name = models.CharField(max_length=200)
      number = models.CharField(max_length=40)
      cats = models.ForeignKey(ModelCategory, on_delete=models.CASCADE)
      city = models.ForeignKey(RegionName, on_delete=models.CASCADE)



      def __str__(self):
          return self.full_name


class CardCategory(models.Model):
      name = models.CharField(max_length=300, verbose_name="karta tarafi")

      def __str__(self):
          return self.name

      class Meta:
            verbose_name = "Karta Categoriya"
            ordering = ['id']


class BusCard(models.Model):
      name  = models.CharField(max_length=200, verbose_name="karta nomi")
      image  = models.ImageField(upload_to='card/')
      f_name  =  models.CharField(max_length=40, verbose_name="tarif rejasi")
      f_name1 = models.CharField(max_length=300, verbose_name="tarif bolimi")
      cat  =  models.ManyToManyField(CardCategory, related_name="k_turlar", blank=True)
      cat1  = models.ManyToManyField(CardCategory, related_name="b_turlari", blank=True)


      def __str__(self):
          return self.name

      class Meta:
            verbose_name = "Karta tarifi"
            verbose_name_plural = "Karta tariflari"
            ordering = ['id']





