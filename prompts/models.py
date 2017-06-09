from django.db import models


class Prompt(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class PromptComment(models.Model):
    title = models.ForeignKey(Prompt)
    link = models.URLField()
    comment = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.author
