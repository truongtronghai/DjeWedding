from django.db import models
from django.utils.html import format_html


# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_text_1 = models.CharField(max_length=200, blank=True, null=True)
    short_text_2 = models.CharField(max_length=200, blank=True, null=True)
    short_text_3 = models.CharField(max_length=200, blank=True, null=True)
    short_text_4 = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def getImageTag(self):
        if self.image:
            return format_html('<img src="%s" alt="%s" title="%s" width="100px" />' % (self.image.url, self.title, self.title))

        return format_html('<img src="" alt="no image" />')
