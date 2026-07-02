
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
        fields = ['is_active','id',"name"]

class TeamFilter(BaseFilter): 
    federation = filters.CharFilter(field_name="federation", lookup_expr="icontains")
    year_founded = filters.NumberFilter(field_name="year_founded", lookup_expr="exact")

    class Meta:
        model = models.Team
        fields = ['is_active','id','name', 'year_founded']

class PersonFilter(BaseFilter):
    birth_date = filters.DateFilter(field_name='birth_date', lookup_expr='exact')
    height = filters.NumberFilter(field_name='height', lookup_expr='exact')
    weight = filters.NumberFilter(field_name='weight', lookup_expr='exact')
    shirt_size = filters.CharFilter(field_name='shirt_size', lookup_expr='icontains')
    foot_size = filters.CharFilter(field_name='foot_size', lookup_expr='icontains')

    class Meta:
        abstract =  True
        fields = ['is_active','id','name','birth_date','height','shirt_size', 'foot_size'] 


class PlayerFilter(PersonFilter):
    foot_size = filters.NumberFilter(field_name="foot_size", lookup_expr="icontains")
    class Meta:
        model = models.Player
        fields = ['is_active','id','foot_size']


class CoachFilter(PersonFilter):
    team__name = filters.CharFilter(field_name="team__name", lookup_expr="icontains")
    class Meta:
        model = models.Coach
        fields = ['is_active','id', 'name', 'team__name'] 
