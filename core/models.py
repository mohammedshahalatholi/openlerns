from django.db import models
from django.utils.text import slugify

class SiteConfiguration(models.Model):
    site_title = models.CharField(max_length=200, default="CheatSheets Hub")
    site_owner = models.CharField(max_length=200, default="Reference from OpenLern")
    site_owner_link = models.URLField(blank=True, default="https://openlern.com")
    site_description = models.TextField(default="The ultimate collection of developer cheat sheets.")

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def save(self, *args, **kwargs):
        # Implement Singleton: Only one instance allowed
        if not self.pk and SiteConfiguration.objects.exists():
            # If you want to prevent creation, you can raise an error
            # Or just update the existing one (more complex logic needed)
             return SiteConfiguration.objects.first()
        return super(SiteConfiguration, self).save(*args, **kwargs)

    def __str__(self):
        return "Site Configuration"

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome class or similar", default="fa-solid fa-folder")
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['ordering', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='technologies', on_delete=models.CASCADE, null=True, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome class or similar")
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CheatSheet(models.Model):
    TYPE_CHOICES = (
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('link', 'Link'),
    )

    title = models.CharField(max_length=200)
    technology = models.ForeignKey(Technology, related_name='cheatsheets', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    file_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='link')
    url = models.URLField(blank=True, help_text="External link URL")
    file = models.FileField(upload_to='cheatsheets/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
