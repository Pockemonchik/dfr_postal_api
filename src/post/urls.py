from post.views import LettersViewSet, ParcelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'letters', LettersViewSet, basename='letters')
router.register(r'parsels', ParcelViewSet, basename='letters')
urlpatterns = router.urls

