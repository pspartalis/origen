from django.db import models

# Create your models here.
class Opportunity(models.Model):
    OPPORTUNITY_TYPE = [
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('training', 'Training'),
        ('course', 'Course'),
    ]

    OPPORTUNITY_CATEGORY = [
        ('per_dev', 'Personal Development'),
        ('marketing', 'Marketing'),
        ('startups', 'Startups'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='opportunities/images/')
    type = models.CharField(max_length=20, choices=OPPORTUNITY_TYPE, default='seminar')
    category = models.CharField(max_length=20, choices=OPPORTUNITY_CATEGORY, default='per_dev')
    online = models.BooleanField()
    cta_link = models.URLField()
    organizer = models.CharField(max_length=200)
    dateAdded = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__ (self):
        return self.title