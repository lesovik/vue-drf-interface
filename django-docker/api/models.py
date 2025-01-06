from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        SUSPENDED = "sus", _('Suspended')
        DELETED = "deleted", _('Deleted')

    first_name = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Queue(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', _('New')
        COMPLETED = "completed", _('Completed')
        PROCESSING = "processing", _('Processing')

    name = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=False,
    )

    def __str__(self):
        return str(self.name)
