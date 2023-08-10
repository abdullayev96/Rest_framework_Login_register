
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework.response import Response
from .models import *

from rest_framework.generics import  ListAPIView

from hitcount.views  import HitCountJSONView


# class Yangilik_ApiView(APIView):
#     def get(self, request):
#         # lst = Yangilik.objects.all().values()
#         # return Response({'posts':list(lst)})
#         w = Yangilik.objects.all()
#         return Response({'posts':YangilikSerializer(w, many=True).data})
#
#
#     def post(self, request):
#         serializer = YangilikSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # post_new = Yangilik.objects.create(
#         #     title = request.data['title'],
#         #     content = request.data['content'],
#         #     cat_id = request.data['cat_id'],
#         # )
#         # print(post_new)
#
#         return Response({"posts": serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Put not allowed"})
#         try:
#             instance = Yangilik.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects not exists"})
#
#         serializer = YangilikSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"posts": serializer.data})
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Delete not allowed"})
#
#         return Response({"posts":" Don't delete post now  " +str(pk)})


class PartnersApi(ListAPIView):
          queryset = Partners.objects.all()
          serializer_class = PartnerSerializer
          permission_classes = [IsAuthenticatedOrReadOnly]
