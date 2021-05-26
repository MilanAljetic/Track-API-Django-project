from rest_framework import serializers

from track_app.models import Track


class TrackSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    class Meta:
        model = Track
        fields = '__all__'
