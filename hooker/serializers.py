from rest_framework import serializers


class HookerSerializer(serializers.Serializer):
    """
    Sample hook serializer

    """
    name = serializers.CharField(
                    required=False,
                    allow_blank=True,
                    max_length=255,
                    )
    short_message = serializers.CharField(
                    required=False,
                    allow_blank=True,
                    max_length=255,
                    )
