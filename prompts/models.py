from django.db import models
from django.urls import reverse


class Prompt(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prompts:detail', kwargs={'slug': self.slug})


class PromptComment(models.Model):
    title = models.ForeignKey(Prompt)
    author = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    story = models.TextField()

    def __str__(self):
        return self.author

    def prompt_url(self):
        url = self.title.link + self.slug
        return url
