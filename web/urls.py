from rest_framework import routers

from .views import BlogsViewSet, ManhwaListViewSet, ManhwaViewSet, TagsViewSet

router = routers.DefaultRouter()
router.register(r"manhwa", ManhwaViewSet)
router.register(r"list", ManhwaListViewSet)
router.register(r"tags", TagsViewSet)
router.register(r"blogs", BlogsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
