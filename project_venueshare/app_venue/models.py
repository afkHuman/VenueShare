from django.db import models

# Create your models here.
class Venues(models.Model):
    idNumber = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    venueType = models.CharField(max_length=255,choices=[
        ('', 'Select type'),
        ('office', 'Office'),
        ('meeting_room', 'Meeting Room'),
        ('conference_hall', 'Conference Hall'),
        ('event_space', 'Event Space'),
        ('other', 'Other'),
        ],
        default="")
    size = models.CharField(max_length=10, verbose_name="Size m²", default="0", blank=True)
    capacity = models.CharField(max_length=10, verbose_name="Capacity", default="0", blank=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"ID: {self.idNumber}"