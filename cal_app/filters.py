# django imports
import django_filters
from django_filters import CharFilter
# local imports
from .models import Food


class FoodFilter(django_filters.FilterSet):
	""" used filter to fetch food item  """
	food_name = CharFilter(field_name = 'name' , lookup_expr = 'icontains',label='search food items')
	class Meta:
		model = Food
		fields = ['food_name']
