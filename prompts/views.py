from django.shortcuts import render
from django.views import generic

from .models import Prompt


class PromptListView(generic.ListView):
    model = Prompt

class PromptDetailView(generic.DetailView):
    model = Prompt
