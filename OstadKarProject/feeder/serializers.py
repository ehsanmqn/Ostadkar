from rest_framework_mongoengine import serializers
from OstadKarProject.feeder.models import Feed

class FeedSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
