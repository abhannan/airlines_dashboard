
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from airlines_dashboard import settings


urlpatterns = [
    url(r'^$', views.AirlineSpecificDashboard.as_view(), name='airline_dashboard'),

    #Financial Data
    url(r'^api/v1/financial_data/airline_specific', 
        views.AirlineSpeceficYearlyFinancialData.as_view(), 
        name='airline_specific_filtered_financial'), # Filtered Data
    url(r'^api/v1/financial_data/$', 
    	views.ListFinancialData.as_view(), 
    	name='financial_data'), # Complete Data

    #Stats Data
    url(r'^api/v1/stats_data/airline_specific', 
        views.AirlineSpeceficYearlyStatsData.as_view(), 
        name='airline_specific_filtered_stats'), # Filtered Data
    url(r'^api/v1/stats_data/$', 
    	views.ListStatsData.as_view(), 
    	name='stats_data'), # Complete Data
]