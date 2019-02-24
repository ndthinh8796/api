from django.shortcuts import render
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeList(APIView):

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self):
        pass
