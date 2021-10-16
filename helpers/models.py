from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=False, null=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.CharField(
        max_length=255, default="None", blank=False, null=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
