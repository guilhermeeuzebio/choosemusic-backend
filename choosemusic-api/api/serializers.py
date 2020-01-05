from rest_framework import serializers

from core.models import Music


class MusicSerializer(serializers.ModelSerializer):
    """ `Serializer` of class 'Music'
        `Serializer` that convet complex class 'Music' in simple type (JSON)
        """
    class Meta:
        model = Music
        fields = [
            'id',
            'music',
            'votes'
        ]
