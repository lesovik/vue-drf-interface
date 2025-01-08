from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


class ObjectStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    SUSPENDED = "suspended", _('Suspended')
    DELETED = "deleted", _('Deleted')



class Customer(models.Model):
    name = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=20, choices=ObjectStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    sort_order = models.IntegerField(unique=True, null=True)

    def get_new_default(self):
        if EquipmentType.objects.all().count() == 0:
            new_order_default = 1
        else:
            new_order_default = EquipmentType.objects.all().aggregate(Max('sort_order'))['sort_order__max'] + 1
        return new_order_default

    def save(self, *args, **kwargs):
        if not self.sort_order:
            self.sort_order = self.get_new_default()
        super(EquipmentType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipment(models.Model):

    name = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=20, choices=ObjectStatus.choices)
    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.PROTECT,
        blank=False,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Queue(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', _('New')
        COMPLETED = "completed", _('Completed')
        PROCESSING = "processing", _('Processing')

    name = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        blank=False,
    )

    def __str__(self):
        return str(self.name)
