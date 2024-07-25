from cats.views import AchievementViewSet, CatViewSet
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore
from rest_framework import routers  # type: ignore

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

api_urlpatterns: list[path] = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),  # Работа с пользователями
    path('', include('djoser.urls.authtoken')),  # Работа с токенами
]

urlpatterns: list[path] = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
