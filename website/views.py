from rest_framework.response import Response
from django.core import serializers
from .models import IotItem
from .serializers import IotItemSerializer
from rest_framework.views import APIView
from django.http.response import HttpResponse


def arduino_get(request):
    item = IotItem.objects.get(port=2)
    value = str(int(item.value))
    return HttpResponse("RED_LED: "+value)


class IotItemsView(APIView):
    queryset = IotItem.objects.all()
    serializer_class = IotItemSerializer

    def get(self, request):
        items = IotItem.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = IotItemSerializer(items, many=True)
        return Response({"items": serializer.data})

    def put(self, request, port):

        item_saved = IotItem.objects.get(port=port)

        data = request.data.get('item')

        serializer = IotItemSerializer(instance=item_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Item '{}' updated successfully".format(item_saved.name)})

