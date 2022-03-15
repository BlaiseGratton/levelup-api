from django.http import HttpResponseServerError
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from levelupapi.models import Status, Event
from levelupapi.views.event import StatusDetailSerializer, EventSerializer
from levelupapi.serializers import StatusSerializer


class StatusView(ViewSet):
    """
        pokemon statuses
    """
    # e.g. http://localhost:8000/statuses
    def list(self, request):
        """
        list view for statuses
        """
        statuses = Status.objects.all()

        try:
            serializer = StatusSerializer(
                            statuses,
                            many=True,
                            context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            
    # e.g. http://localhost:8000/statuses/3
    def retrieve(self, request, pk=None):
        try:
            status = Status.objects.get(pk=pk)
            serializer = StatusDetailSerializer(status, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @action(methods=['get'], detail=True, permission_classes=[IsAdminUser])
    def events(self, request, pk=None):
        try:
            username = request.query_params.get('username')

            if username:
                events = Event.objects.filter(
                    status_id=pk, 
                    organizer__user__first_name=username)
            else:
                events = Event.objects.filter(status_id=pk)
            serializer = EventSerializer(events, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)