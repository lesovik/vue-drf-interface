from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Queue, Customer, EquipmentType, Equipment
from .serializers import QueueSerializer, CustomerSerializer, EquipmentSerializer, EquipmentTypeSerializer


class QueueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queues to be viewed or edited.
    """
    queryset = Queue.objects.all().order_by('-created_at')
    serializer_class = QueueSerializer
    permission_classes = []

    def get_queryset(self):
        sorter = get_sorter(
            Queue._meta.get_fields(),
            self.request.query_params,
            '-created_at'
        )
        if len(sorter):
            return Queue.objects.all().order_by(*sorter)
        return Queue.objects.all().order_by('-created_at')


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = []


    filter_backends = (SearchFilter,)
    search_fields = ['name']

    def get_queryset(self):
        sorter = get_sorter(
            Customer._meta.get_fields(),
            self.request.query_params,
            'id'
        )
        if len(sorter):
            return Customer.objects.order_by(*sorter)
        return Customer.objects.order_by('-created_at')


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Equipment to be viewed or edited.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = []

    def get_queryset(self):
        sorter = get_sorter(
            Equipment._meta.get_fields(),
            self.request.query_params,
            'id'
        )
        if len(sorter):
            return Equipment.objects.all().order_by(*sorter)
        return Equipment.objects.all().order_by('id')


class EquipmentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows equipment types to be viewed or edited.
    """
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    permission_classes = []

    filter_backends = (SearchFilter,)
    search_fields = ['name']

    def get_queryset(self):
        sorter = get_sorter(
            EquipmentType._meta.get_fields(),
            self.request.query_params,
            'id'
        )
        if len(sorter):
            return EquipmentType.objects.order_by(*sorter)
        return EquipmentType.objects.order_by('sort_order')


def get_sorter(fields, values, default=None):
    sorter = []
    names = [field.name for field in fields]
    for key in values.keys():
        value = values.get(key)
        sort_key = key.replace('sort_', '')
        if sort_key in names:
            if value != '':
                if value == 'desc':
                    sorter.append('-' + sort_key)
                else:
                    sorter.append(sort_key)
    if default is not None and len(sorter) == 0:
        sorter.append(default)
    return sorter
