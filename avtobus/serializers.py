from rest_framework import serializers
from  .models import *



class AvtobusYearSerializer(serializers.ModelSerializer):

          cat_name = serializers.SerializerMethodField()
          class Meta:
                model  = AvtobusYear
                fields = ['id','cat_name', 'name', 'title','image']



          def get_cat_name(self, obj):
              if obj.cat:
                 return obj.cat.name
              return None


class AvtobusYearDetailSerializer(serializers.ModelSerializer):

          class Meta:
                model  = AvtobusYear
                fields = ['name', 'image', 'born_year', 'size', 'seat_count', 'number_direction', 'content']




class  AvtoBackSerializer(serializers.ModelSerializer):
          class Meta:
                model = AvtobusBackground
                fields = ['id', 'number', 'direction', 'startend', 'sideways_time', 'route_length', 'bus_brand', 'place']



class AvtoDataSerializer(serializers.ModelSerializer):
          class Meta:
                model = AvtobusData
                fields   = ['id', 'avto_number', 'start_place', 'end_place', 'fast_time']




class BusListSerializer(serializers.ModelSerializer):
      cat_name = serializers.SerializerMethodField()
      images = serializers.SerializerMethodField()


      def get_cat_name(self, obj):
          if obj.cat:
              return obj.cat.name
          return None


      def get_images(self, obj):
          images = obj.images.all().values_list('image', flat=True)
          return images


      class Meta:
          model = BusOrder
          fields = ['cat_name', 'size', 'price', 'images']




class OrderPostSerializer(serializers.ModelSerializer):

      class Meta:
            model = OrderPost
            fields =  ["full_name", "number", "cats", "city"]



class CardSerializer(serializers.ModelSerializer):
      cat_name  = serializers.SerializerMethodField()
      cat_names = serializers.SerializerMethodField()


      class Meta:
            model = BusCard
            fields   = ['id','image', 'name', 'f_name','cat_name',  'f_name1','cat_names']

      def get_cat_name(self, obj):
          cat_name = obj.cat.all().values_list('name', flat=True)
          return cat_name


      def get_cat_names(self, obj):
          cat_names = obj.cat1.all().values_list('name', flat=True)
          return cat_names




