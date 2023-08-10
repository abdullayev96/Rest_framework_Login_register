from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):

      class Meta:
            model  = News
            fields  = ['id', 'image_one', 'created', 'name']



class NewsDetailSerializers(serializers.ModelSerializer):
          views = serializers.SerializerMethodField()
          images =serializers.SerializerMethodField()



          class Meta:
                model  = News
                fields  = ['name', 'created', 'views', 'images', 'body']



          def get_views(self, obj):
                    return obj.views.count()


          def get_images(self, obj):
              image = obj.images.all().values_list('image', flat=True)
              return image


class BabySerializer(serializers.ModelSerializer):
      class Meta:
            model  = BigNewsBaby
            fields  = ['name', 'image', 'body', 'leader_name', 'address','number']