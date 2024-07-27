from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from drf_cache import CacheResponseMixin

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AchievementViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
