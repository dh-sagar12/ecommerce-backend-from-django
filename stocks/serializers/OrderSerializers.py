from rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from stocks.models.OrderModels import OrdersModel
from django.db import transaction

from stocks.serializers.DeliveryAddressSerializer import DeliveryAdressSerializer
from  rest_framework.fields import CurrentUserDefault




class ProductOrderSerializer(ModelSerializer):
    
    class Meta:
        model =  OrdersModel
        fields  = [ "id", "product_id", "product_inventory_id", "order_qty", "ordered_by", "ordered_date", "payment_method", "is_payment_completed", "created_on", "updated_on", "delivered_date", "cart_id"]
        read_only_fields = ['id', 'created_on', "updated_on"]



class SingleProductOrderSerializer(ModelSerializer):
    order  =  serializers.JSONField()
    delivery_address =  serializers.JSONField()
    
    class Meta:
        model = OrdersModel
        fields =  ['order', 'delivery_address']

    
    
    @transaction.atomic
    def create(self, validated_data):
        order  =  validated_data.pop('order')
        delivery_address =  validated_data.pop('delivery_address')
        
        order_serializer  =  ProductOrderSerializer(data=order)
        order_serializer.is_valid(raise_exception= True)
        order_instance  =  order_serializer.save()

        delivery_address['order_id'] =  order_instance.id
        delivery_address_serialzer  =  DeliveryAdressSerializer(data=delivery_address)
        delivery_address_serialzer.is_valid(raise_exception=True)
        delivery_address_serialzer.save()
        return order_instance



class CartOderSerializer(ModelSerializer):
    order  =  serializers.ListField()
    delivery_address =  serializers.JSONField()

    class Meta:
        model =  OrdersModel
        fields =  ['order', 'delivery_address']


    def get_ordered_by(self, obj):
        return self.context['request'].user

    @transaction.atomic
    def create(self, validated_data):
        order  =  validated_data.pop('order')
        delivery_address =  validated_data.pop('delivery_address')
        
        
        for item in order:
            # item['ordered_by'] =  1
            order_serializer  =  ProductOrderSerializer(data=item)
            order_serializer.is_valid(raise_exception= True)
            order_instance  =  order_serializer.save()
            delivery_address['order_id'] =  order_instance.id
            delivery_address_serialzer  =  DeliveryAdressSerializer(data=delivery_address)
            delivery_address_serialzer.is_valid(raise_exception=True)
            delivery_address_serialzer.save()
        return order_instance


    


   