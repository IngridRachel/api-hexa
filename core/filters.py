
from core import models
from django_filters import rest_framework as filters


class BaseFilter(filters.FilterSet):
    name =  filters.CharFilter(field_name="name",lookup_expr="icontains")
    id = filters.NumberFilter(field_name="id",lookup_expr="exact")
    is_active = filters.BooleanFilter(field_name="is_active",lookup_expr="exact")

    class Meta:
        abstract =  True

class TeamGroupFilter(BaseFilter):

    class Meta:
        model = models.TeamGroup
        fields = ["name"]

class TeamFilter(BaseFilter): 
    federation = filters.CharFilter(field_name="federation", lookup_expr="icontains")
    year_founded = filters.NumberFilter(field_name="year_founded", lookup_expr="exact")

    class Meta:
        model = models.Team
        fields = ['is_active', 'year_founded']

class PersonFilter(BaseFilter):
    birth_date = filters.DateFilter(field_name='birth_date', lookup_expr='exact')
    height = filters.NumberFilter(field_name='height', lookup_expr='exact')
    weight = filters.NumberFilter(field_name='weight', lookup_expr='exact')

    class Meta:
        abstract =  True
        fields = ['is_active', 'shirt_size'] 


class PlayerFilter(PersonFilter):
    foot_size = filters.NumberFilter(field_name="foot_size", lookup_expr="icontains")
    class Meta:
        model = models.Player
        fields = ['position','foot_preference']


class CoachFilter(PersonFilter):
    class Meta:
        model = models.Coach
        fields = ['is_active', 'shirt_size'] 
