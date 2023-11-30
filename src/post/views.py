from rest_framework import viewsets
from .serializers import *
from config.settings import *
from .models import *
from config.settings import *
from rest_framework.permissions import AllowAny


class LettersViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с письмами.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [AllowAny]

class ParcelViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с посылками.
    """
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [AllowAny]









