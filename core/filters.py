from core import models
from django_filters import rest_framework as filters

class BaseFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    is_active = filters.BooleanFilter(field_name="is_active", lookup_expr="exact")

    class Meta:
        abstract = True

class TeamGroupFilter(BaseFilter):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        models = models.TeamGroup
        fields = ["name"]