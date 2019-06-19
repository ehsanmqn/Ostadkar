from django.conf.urls import url, include
from django.urls import path

from rest_framework_mongoengine import routers
from OstadKarProject.feeder.views import FeedViewSet

router = routers.DefaultRouter()
router.register(r'feeder', FeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns += merouter.urls
