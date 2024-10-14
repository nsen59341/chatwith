from django.db import models
from datetime import datetime

# Create your models here.
class Msg(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    sender = models.CharField(max_length=255, default='Guest')
    msg = models.TextField(default='')
    lastSent = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.sender 