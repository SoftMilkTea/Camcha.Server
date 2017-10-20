from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from application.models import Detection
from application.serializers import DetectionSerializer


# Create your views here.
class DetectionList(generics.ListCreateAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetectionDetail(APIView):

    def get(self, request, pk, format=None):
        detection = get_object_or_404(Detection,pk=pk)
        serializer = DetectionSerializer(detection)
        return Response(serializer.data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'detections': reverse('detection-list',request=request, format=format)
    })

def detection_map(request):
    detections = Detection.objects.all()
    context = {
        "detections" : detections
    }
    return render(request,"application/detection_map.html",context)




