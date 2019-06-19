from django.shortcuts import render

from rest_framework_mongoengine import viewsets as meviewsets
from OstadKarProject.feeder.serializers import FeedSerializer
from OstadKarProject.feeder.models import Feed

class FeedViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
