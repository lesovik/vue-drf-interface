from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


def get_sort_order_default(queryset):
    if queryset.count() == 0:
        new_order_default = 1
    else:
        new_order_default = queryset.aggregate(Max('sort_order'))['sort_order__max'] + 1
    return new_order_default


class RecordStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    SUSPENDED = "suspended", _('Suspended')
    DELETED = "deleted", _('Deleted')


class UniquelyNamed(models.Model):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        abstract = True


class DatedRecord(models.Model):
    record_status = models.CharField(max_length=20, choices=RecordStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SortOrdered(models.Model):
    sort_order = models.IntegerField(unique=True, null=True)

    class Meta:
        abstract = True


class Described(models.Model):
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        abstract = True


class Customer(UniquelyNamed, Described, DatedRecord):

    def __str__(self):
        return self.name


class EquipmentType(UniquelyNamed, SortOrdered, Described):

    def save(self, *args, **kwargs):
        if not self.sort_order:
            self.sort_order = get_sort_order_default(EquipmentType.objects.all())
        super(EquipmentType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class EquipmentStatus(UniquelyNamed, SortOrdered, Described):

    def save(self, *args, **kwargs):
        if not self.sort_order:
            self.sort_order = get_sort_order_default(EquipmentStatus.objects.all())
        super(EquipmentStatus, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipment(UniquelyNamed, Described, DatedRecord):
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

    def __str__(self):
        return self.name


class Queue(UniquelyNamed, Described, DatedRecord):
    class Status(models.TextChoices):
        NEW = 'new', _('New')
        COMPLETED = "completed", _('Completed')
        PROCESSING = "processing", _('Processing')

    queue_status = models.CharField(max_length=500, choices=Status.choices)
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        blank=False,
    )

    def __str__(self):
        return str(self.name)
