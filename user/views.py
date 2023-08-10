from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from django.http import Http404
from rest_framework import status
import random
import string


def generate_random_string(length):
          characters = string.ascii_letters + string.digits
          verification_code = ''.join(random.choice(characters) for _ in range(length))
          return verification_code


class UserSendApi(APIView):


          def post(self, request):
                    reference_number = random.randint(10000, 99999)
                    verification_code = generate_random_string(10)

                    serializer = SendUserSerializer(data=request.data, context={'request': self.request})
                    serializer.is_valid(raise_exception=True)
                    serializer.save(reference_number=reference_number
                                    , verification_code=verification_code, status=SendUser.NEW)

                    return Response({"reference_number": reference_number, "verification_code": verification_code})


class UserDetailApi(APIView):
          def get(self, request, pk=None):
              if pk:
                   user = SendUser.objects.get(id=pk)
                   serializer = SendAnswerSerializer(user)
                   return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

              user =SendUser.objects.all()
              serializer = SendAnswerSerializer(user, many=True)
              return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)





class AnswerApi(APIView):
     def post(self, request, *args, **kwargs):
          serializers = SendBackSerializer(data=request.data, context={'request': self.request})
          if serializers.is_valid(raise_exception=True):
               reference_number=serializers.data.get('reference_number')
               verification_code = serializers.data.get('verification_code')
               # msg = 'password={}'.format(reference_number)
               # msg1 = 'login={}'.format(verification_code)
               # reference_number = self.request.POST.get("reference_number")
               # verification_code = self.request.POST.get("verification_code")
               send = SendUser.objects.filter(reference_number=reference_number,verification_code=verification_code)
               serializer = SendAnswerSerializer(send, many=True, context={'request': self.request})

               return Response(serializer.data)

               # return Response(serializer.errors)

          else:
               return Response(serializers.errors, status=400)
     #
     # def post(self, request, *args, **kwargs):
     #     reference_number = self.request.POST.get("reference_number")
     #     verification_code = self.request.POST.get("verification_code")
     #     send = SendUser.objects.filter(reference_number=reference_number, verification_code=verification_code)
     #     serializer = SendAnswerSerializer(send, many=True)
     #
     #
     #     return Response(serializer.data)

