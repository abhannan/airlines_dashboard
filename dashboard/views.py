from django.shortcuts import render
from django.views.generic import View
from .models import FinancialData, Airline, Year, StatsData
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinancialDataSerializer, StatsDataSerializer

class AirlineSpecificDashboard(View):

	def get(self, request, *args, **kwargs):
		airline_list = Airline.objects.all()
		year_list = Year.objects.all()
		return render(request, 'dashboard/airline_specific.html', {'airline_list': airline_list, 'year_list': year_list})

class AirlineSpeceficYearlyFinancialData(generics.ListAPIView): # Serialized Filtered Financial Data requested by frontend
	serializer_class = FinancialDataSerializer

	def get_queryset(self, *args, **kwargs):
		airline_category = self.request.GET.get("airline_category")
		year_category = self.request.GET.get("year_category")
		queryset_filtered_airline = FinancialData.objects.filter(airline_id=airline_category)
		queryset_filtered_airline_year = queryset_filtered_airline.filter(financial_year_id=year_category)
		return queryset_filtered_airline

class ListFinancialData(generics.ListCreateAPIView): # Complete Serialized Financial Data
	queryset =FinancialData.objects.all()
	serializer_class = FinancialDataSerializer

class AirlineSpeceficYearlyStatsData(generics.ListAPIView): # Serialized Filtered Stats Data requested by frontend
	serializer_class = StatsDataSerializer

	def get_queryset(self, *args, **kwargs):
		airline_category = self.request.GET.get("airline_category")
		year_category = self.request.GET.get("year_category")
		queryset_filtered_airline = StatsData.objects.filter(airline_id=airline_category)
		queryset_filtered_airline_year = queryset_filtered_airline.filter(financial_year_id=year_category)
		return queryset_filtered_airline

class ListStatsData(generics.ListCreateAPIView): # Complete Serialized Financial Data
	queryset =StatsData.objects.all()
	serializer_class = StatsDataSerializer
