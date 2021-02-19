from rest_framework import serializers

from core.models import (Shipper, DesignAppendCategory,
                         DesignAppend, OrderItem, Order)


class ShipperSerializer(serializers.ModelSerializer):
    """Serializer for shipper object"""

    class Meta:
        model = Shipper
        fields = ('id', 'company_name')
        read_only_fields = ('id',)


class DesignAppendCategorySerializer(serializers.ModelSerializer):
    """Seializer for OrderItemAppendCategory object"""

    class Meta:
        model = DesignAppendCategory
        fields = ('id', 'type_name')
        read_only_fields = ("id",)


class DesignAppendSerializer(serializers.ModelSerializer):
    """Serializer for OrderItemAppend objects"""

    class Meta:
        model = DesignAppend
        fields = ('id', 'name', 'image', 'design_append_category',
                  'design_append_price_irr')
        read_only_fields = ('id',)


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem objects"""
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id',)

    # def create(self, validated_data):


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order objectrs"""
    class Meta:
        model = Order
        fields = ("id", "create_order_datetime", "shipper_date", "paid_datetime", "paid", "deleted",
                  "first_name", "last_name", "address1", "address2", "phone", "age", "city", "province", "postal_code", "country")
        read_only_fields = ('id',)
