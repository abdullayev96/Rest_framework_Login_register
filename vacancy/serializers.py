from  rest_framework  import serializers
from .models import *



class VacancySerializer(serializers.ModelSerializer):
      cat_name   = serializers.SerializerMethodField()
      class Meta:
            model  = Vacancy
            fields  = ['id', 'name', 'created', 'cat_name', 'experience']

      def get_cat_name(self, obj):
            if obj.cat:
                  return obj.cat.name
            return None


class DetailVacancySerializer(serializers.ModelSerializer):
      views  = serializers.SerializerMethodField()
      class Meta:
            model  = Vacancy
            fields  = ['name', 'created', 'views', 'title', 'number']

      def get_views(self, obj):
            return obj.views.count()