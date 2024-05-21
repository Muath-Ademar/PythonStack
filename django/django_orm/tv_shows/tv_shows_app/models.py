from django.db import models


class Network (models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Show (models.Model):
    title = models.CharField(max_length=45)
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE, null=True)
    release_date = models.DateTimeField()
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

