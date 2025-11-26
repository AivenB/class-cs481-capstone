import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

# Test Tutorial Model
class Testing(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Survey/Assessment Models
class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    example = models.TextField(blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name="questions")
    characteristics = models.ManyToManyField(Characteristic, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Tracks edits to question wording

    def __str__(self):
        return f"{self.text[:60]}..."


class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Community(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Assessment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('community', 'survey')

    def __str__(self):
        return f"{self.community.name} | {self.survey.name}"


class Response(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    # assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE)
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('assessment', 'question')