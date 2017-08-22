from django.db import models

class Airline(models.Model):
	name = models.CharField(max_length=10, blank=True, null=True)
	code = models.CharField(max_length=2, blank=True, null=True)
	def __str__(self):
		return self.name

class Year(models.Model):
	YEARS_CHOICE = (
		(2012, 2012),
		(2013, 2013),
		(2014, 2014),
		(2015, 2015),
		(2016, 2016),
		)
	year = models.IntegerField(choices=YEARS_CHOICE, blank=True, null=True)

	def __str__(self):
		return str(self.year)

class FinancialData(models.Model): # All units in millions
	airline = models.ForeignKey(Airline)
	financial_year = models.ForeignKey(Year)
	mainline_revenue = models.DecimalField(max_digits=7, decimal_places=2)
	regional_revenue = models.DecimalField(max_digits=7, decimal_places=2)
	other_revenue = models.DecimalField(max_digits=7, decimal_places=2)
	total_revenue = models.DecimalField(max_digits=7, decimal_places=2)
	salaries_wages = models.DecimalField(max_digits=7, decimal_places=2)
	aircraft_fuel = models.DecimalField(max_digits=7, decimal_places=2)
	depreciation_amortization = models.DecimalField(max_digits=7, decimal_places=2)
	interest_expense = models.DecimalField(max_digits=7, decimal_places=2)
	other_expenses = models.DecimalField(max_digits=7, decimal_places=2)
	operating_expenses = models.DecimalField(max_digits=7, decimal_places=2)
	operating_result = models.DecimalField(max_digits=7, decimal_places=2)
	non_operating_items = models.DecimalField(max_digits=7, decimal_places=2)
	net_result = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return str(self.mainline_revenue)

class StatsData(models.Model):
	airline = models.ForeignKey(Airline)
	financial_year = models.ForeignKey(Year)
	block_hours = models.DecimalField(max_digits=6, decimal_places=2) # in thousands
	flight_hours = models.DecimalField(max_digits=6, decimal_places=2) # in thousands
	departures = models.DecimalField(max_digits=6, decimal_places=2) # in thousands
	rev_pax_miles = models.DecimalField(max_digits=7, decimal_places=4) # in billions
	avail_seat_miles = models.DecimalField(max_digits=7, decimal_places=4) # in billions
	fuel_gallons = models.DecimalField(max_digits=6, decimal_places=2) # in millions

	def __str__(self):
		return str(self.block_hours)

