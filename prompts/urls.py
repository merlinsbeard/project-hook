from django.conf.urls import url
from . import views


app_name = 'prompts'

urlpatterns = [
    # /
    # /prompts/
    url(r'^$', views.PromptListView.as_view(), name='list'),
#    url(r'^(?P<slug>[-\w]+)/$',
#        views.WorkDetailView.as_view(), name='detail'),
]
