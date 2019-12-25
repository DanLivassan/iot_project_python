from django.db import models


class IotItem(models.Model):
    name = models.fields.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
    value = models.fields.BooleanField(default=True)
    port = models.fields.IntegerField(null=True)

    def __str__(self):
        return self.name
