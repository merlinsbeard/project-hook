from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PromptAPIListView, PromptCommentAPIView, PromptSlug


urlpatterns = [
        url(r'^prompts/$', PromptAPIListView.as_view()),
        url(r'^comments/$', PromptCommentAPIView.as_view()),
        url(r'^prompts/slug/$', PromptSlug.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
