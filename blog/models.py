from django.db import models
from django.utils import timezone

# Create your models here.
FMT_CHOICES = (
    ('TEXT', 'Text'),
    ('MARKDOWN', 'Markdown'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   

class Post2(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    f_choice =  models.CharField(max_length=8, choices=FMT_CHOICES, default='TEXT',)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   
        
