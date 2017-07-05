from rest_framework import serializers
from prompts.models import Prompt, PromptComment


class PromptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prompt
        fields = ('title', 'slug')

class PromptCommentSerializer(serializers.ModelSerializer):
    title= PromptSerializer()

    class Meta:
        model = PromptComment
        fields = ('title',
                  'author',
                  'slug',
                  'story')

    def create(self, validated_data):
        title = validated_data.pop('submission')
        title = Prompt.objects.create(**title)
        validated_data['title'] = title
        comment = PromptComment.objects.create(**validated_data)
        return comment

class PromptSlugSerializer(serializers.Serializer):
    slug = serializers.CharField(max_length=255)
