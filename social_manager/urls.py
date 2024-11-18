from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import SocialMediaAccountViewSet, ScheduledPostViewSet

router = DefaultRouter()
router.register(r'accounts', SocialMediaAccountViewSet)
router.register(r'posts', ScheduledPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
