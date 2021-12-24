from django.urls import include, path
from rest_framework import routers
from .views import ManhwaViewSet, ManhwaListViewSet, TagsViewSet

router = routers.DefaultRouter()
router.register(r"manhwa", ManhwaViewSet)
router.register(r"list", ManhwaListViewSet)
router.register(r"tags", TagsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
