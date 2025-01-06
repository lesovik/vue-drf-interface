from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Customer, Queue


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    label = serializers.SerializerMethodField('set_label')

    def set_label(self, instance):
        return instance.first_name
    class Meta:
        model = Customer
        fields = ['id','label', 'first_name', 'status', 'created_at', 'updated_at']

class QueueCustomerSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField('set_label')

    def set_label(self, instance):
        return instance.first_name

    class Meta:
        model = Customer
        fields = ['id', 'label']
        extra_kwargs = {
            'id': {'read_only': False},
            'label': {'read_only': False},
        }


class QueueSerializer(serializers.HyperlinkedModelSerializer):
    customer = QueueCustomerSerializer()

    class Meta:
        model = Queue
        fields = ['id', 'name', 'status', 'customer', 'created_at', 'updated_at']

    def validate_customer(self, obj):
        customer = Customer.objects.filter(pk=obj.get('id'))
        if customer:
            return customer[0]
        raise ValidationError('No such customer!')

    def update(self, instance, validated_data):
        if self.is_valid():
            for key in validated_data.keys():
                setattr(instance, key, validated_data.get(key))
            instance.save()
        return instance
