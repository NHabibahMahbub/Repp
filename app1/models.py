from django.db import models


# Create your models here.
class Platform(models.Model):
    property_type_choices = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('industrial', 'Industrial'),
        ('special_purpose', 'Special Purpose')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=property_type_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size_sqft = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='property_images/')
    listed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
