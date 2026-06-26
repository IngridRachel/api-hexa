from rest_framework import viewsets
from core import models, serializer
 

class TeamGroupViewSet(viewsets.ModelViewSet):
    queryset= models.TeamGroup.objects.all()
    serializer_class = serializer.TeamGroupSerialzer

class TeamViewSet(viewsets.ModelViewSet):
    queryset =  models.Team.objects.all()
    serializer_class = serializer.TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset =models.Player.objects.all()
    serializer_class = serializer.PlayerSerializer

class CoachViewSet (viewsets.ModelViewSet):
    queryset = models.Coach.objects.all()
    serializer_class = serializer.CoachSerializer
