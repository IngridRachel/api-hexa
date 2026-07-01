from rest_framework import serializers

from core import models


class ModelSeralizer(serializers.ModelSerializer):
    id =serializers.IntegerField(read_only=True)
    is_active =serializers.BooleanField()
    created_at =serializers.DateTimeField(read_only=True)
    updated_at =serializers.DateTimeField(read_only=True)

    class Meta:
        model= models.ModelBase
        fields = "__all__"

class TeamGroupSerialzer(ModelSeralizer):

    class Meta:
        model= models.TeamGroup
        fields = "__all__"

class TeamSerializer(ModelSeralizer):

    class Meta:
        model= models.Team
        fields = "__all__"

class PlayerSerializer(ModelSeralizer):

    class Meta:
        model = models.Player
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["team"] = instance.team.name
        representation['shirt_size'] = instance.get_shirt_size_display()
        representation["position"] = instance.get_position_display()
        representation["foot_preference"] = instance.get_foot_preference()
        return representation
        
    
class CoachSerializer(ModelSeralizer):

    class Meta:
        model = models.Coach
        fields = "__all__"