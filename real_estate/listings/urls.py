from rest_framework.routers import DefaultRouter
from .views import (
    AgentViewSet, PropertyViewSet, PropertyImageViewSet,
    ClientViewSet, BookingViewSet, PropertyTypeViewSet
)

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'property-images', PropertyImageViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
