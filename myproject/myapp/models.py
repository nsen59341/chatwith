from django.db import models

# Create your models here.
class Msg(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    sender = models.CharField(max_length=255, default='Guest')
    receiver = models.CharField(max_length=255, default='Guest')
    msg = models.TextField(default='')

    def __str__(self) -> str:
        return self.sender + ' -> ' + self.receiver