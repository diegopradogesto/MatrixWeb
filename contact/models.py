from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    twitter_account = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)