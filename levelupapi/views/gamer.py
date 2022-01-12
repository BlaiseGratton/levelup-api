from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import serializers

from levelupapi.models import Gamer
from levelupapi.views.event import EventSerializer


@api_view(['GET'])
def get_gamer_profile(request):
    gamer = request.auth.user.gamer

    serializer = GamerSerializer(gamer, context={'request': request})

    return Response(serializer.data)


class GamerSerializer(serializers.ModelSerializer):

    attending = EventSerializer(many=True)

    class Meta:
        model = Gamer
        fields = ('id', 'bio', 'attending')

