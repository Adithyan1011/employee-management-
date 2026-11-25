from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import EmployeeDb
from .serializers import EmployeeSerilier
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegisterrView(APIView):
    def post(self,request):
        serializer_instance = RegisterSerializer(data = request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"Registration successfull.."
            })
        else:
            return Response(serializer_instance.errors)

class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,reuest):
        qs = EmployeeDb.objects.all()
        serializer_instance = EmployeeSerilier(qs,many =True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance = EmployeeSerilier(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"added successfullly"})
        else:
            return Response(serializer_instance.errors)


class EmployeeDeialView(APIView):
    permission_classes = IsAuthenticated
    def get(self,request,pk):
        qs = get_object_or_404(EmployeeDb,id = pk)
        serializer_instance = EmployeeSerilier(qs)
        return Response(serializer_instance.data)


    def put(self,request,pk):
        qs = get_object_or_404(EmployeeDb,id = pk)
        if qs.created_by == request.user:
            serializer_instance= EmployeeSerilier(qs,data = request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(data={
                    "message":"Updated successfully"
                })
            else:
                return Response(serializer_instance.errors,status=403)
        else:
            return Response("access denied!")

    def delete(self,request,pk):
        qs = get_object_or_404(EmployeeDb,id = pk)
        if qs.created_by == request.user:
            qs.delete()
            return Response({"message":" deleted successfully "})
        else:
            return Response({"messgae":"access denied"},status=403)