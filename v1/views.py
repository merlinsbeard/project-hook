from django.shortcuts import render
from .serializers import PromptSerializer, PromptCommentSerializer, PromptSlugSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from prompts.models import Prompt, PromptComment
from .external.reddit import Reddit
from django.conf import settings


class PromptAPIListView(generics.ListAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer


class PromptCommentAPIView(generics.ListAPIView):
    queryset = PromptComment.objects.all()
    serializer_class = PromptCommentSerializer


class PromptSlug(APIView):
    """Save a writtingprompt comment."""

    serializer_class = PromptSlugSerializer

    def post(self, request, *args, **kwargs):
        """Get a request with slug then save its details."""
        slug = request.data['slug']
        reddit_secret = settings.REDDIT_SECRET
        reddit_id = settings.REDDIT_ID
        reddit_username = settings.REDDIT_USERNAME
        reddit_password = settings.REDDIT_PASSWORD

        r = Reddit(reddit_secret, reddit_id,
                   reddit_username, reddit_password)
        comment = r.get_comment_body(slug)
        title ={"title": comment["title"], "slug": comment["slug"]}
        prompt = Prompt.objects.get_or_create(**title)
        prompt = prompt[0]
        detail = comment['prompt']
        data = {"slug": detail["slug"],
                "author": detail["author"],
                "story": detail["story"]}
        data['title'] = prompt
        comment = PromptComment.objects.get_or_create(**data)
        if not comment[1]:
            return Response(
                    {"message":"Already Exists"},
                    status.HTTP_423_LOCKED)
        return Response({"message": "success"})
