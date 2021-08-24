from django.db import models


class Client(models.Model):
    chat_id = models.IntegerField(unique=True)
    user_name =  models.CharField(max_length=150)
    settings = models.JSONField()
    last_viewed = models.CharField(max_length=300)

