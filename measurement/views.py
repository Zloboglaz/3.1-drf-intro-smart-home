# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_serializer_class(self):
        # Можно не переопределять, так как для list и create используется один сериализатор.
        return super().get_serializer_class()


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return SensorSerializer
        return SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
