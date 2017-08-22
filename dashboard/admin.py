from django.contrib import admin
from .models import Airline, Year, FinancialData, StatsData

class FinancialDataAdmin(admin.ModelAdmin):
    model = FinancialData
    list_display = ('airline', 'financial_year','mainline_revenue', 'regional_revenue', 'other_revenue')

class StatsDataAdmin(admin.ModelAdmin):
    model = StatsData
    list_display = ('airline', 'financial_year','block_hours', 'flight_hours', 'departures')

class AirlineAdmin(admin.ModelAdmin):
    model = Airline
    list_display = ('name', 'code')

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Year)
admin.site.register(FinancialData, FinancialDataAdmin)
admin.site.register(StatsData, StatsDataAdmin)
