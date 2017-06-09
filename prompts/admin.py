from django.contrib import admin
from .models import Prompt, PromptComment

admin.site.register(Prompt)
admin.site.register(PromptComment)

