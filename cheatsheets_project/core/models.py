from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CheatSheet(models.Model):
    TYPE_CHOICES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('link', 'Link'),
    ]

    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='cheatsheets')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='cheatsheets/', blank=True, null=True)
    external_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
