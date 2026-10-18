from django.db import models
from django.utils.text import slugify
# from .storages.supabase_storage import SupabaseImageStorage



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project_objective = models.TextField(blank=True, null=True)
    project_scope = models.TextField(blank=True, null=True)
    technology_used = models.TextField(blank=True, null=True)
    challenges_and_solution = models.TextField(blank=True, null=True)
    impact_and_outcome = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Add slug field
    
    def __str__(self):
        return self.name

    def short_description(self):
        """ Return a short preview of the description for display """
        return self.description[:150] + "..." if len(self.description) > 150 else self.description

    def save(self, *args, **kwargs):
        """ Automatically generate the slug from the name field if it is not provided """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def get_slug(self):
        return self.slug  # Return the slug, assuming it exists




class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField( blank=True)  # Add slug field for URL-safe identifiers
    countries = models.ManyToManyField(Country, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    features = models.TextField(help_text="Key features of the service")
    benefits = models.TextField(help_text="Advantages of using this service")
    why_choose_us = models.TextField(help_text="Reasons to choose us over competitors")
    process = models.TextField(help_text="How the service works")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    
    def get_country_slugs(self):
        """Return a list of slugified country names"""
        return [country.get_slug() for country in self.countries.all()]

    def save(self, *args, **kwargs):
        """Override save to auto-generate the slug if it's not set."""
        if not self.slug:
            self.slug = slugify(self.title)  # Generate the slug from the title
        super(Service, self).save(*args, **kwargs)



class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.service.title} by {self.first_name} {self.last_name}"

