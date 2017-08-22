from rest_framework import serializers
from .models import FinancialData, StatsData

class FinancialDataSerializer(serializers.ModelSerializer):
	financial_year = serializers.CharField(source='financial_year.year')
	class Meta:
		model = FinancialData
		fields = (
			# 'airline',
			'financial_year',
			'mainline_revenue',
			'regional_revenue',
			'other_revenue',
			# 'total_revenue',
			'salaries_wages',
			'aircraft_fuel',
			'depreciation_amortization',
			'interest_expense',
			'other_expenses',
			# 'operating_expenses',
			# 'operating_result',
			'non_operating_items',
			# 'net_result',
			)

class StatsDataSerializer(serializers.ModelSerializer):
	financial_year = serializers.CharField(source='financial_year.year')
	class Meta:
		model = StatsData
		fields = (
			# 'airline',
			'financial_year',
			'block_hours',
			'flight_hours',
			'departures',
			'rev_pax_miles',
			'avail_seat_miles',
			'fuel_gallons',
			)
		