from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from core import models, serializer, filters

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]

class TeamGroupViewSet(BaseViewSet):
    queryset= models.TeamGroup.objects.all()
    serializer_class = serializer.TeamGroupSerialzer
    filterset_class = filters.TeamGroupFilter

class TeamViewSet(BaseViewSet):
    queryset =  models.Team.objects.all()
    serializer_class = serializer.TeamSerializer
    filterset_class = filters.TeamFilter

class PlayerViewSet(BaseViewSet):
    queryset =models.Player.objects.all()
    serializer_class = serializer.PlayerSerializer
    filterset_class = filters.PlayerFilter


class CoachViewSet (BaseViewSet):
    queryset = models.Coach.objects.all()
    serializer_class = serializer.CoachSerializer
    filterset_class = filters.CoachFilter