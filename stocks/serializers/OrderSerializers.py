from rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from stocks.models.CartModels import CartModel
from stocks.models.OrderModels import OrdersModel, OrdersStatusModel
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


    def get_ordered_by(self):
        return self.context['request'].user.id

    @transaction.atomic
    def create(self, validated_data):
        order  =  validated_data.pop('order')
        delivery_address =  validated_data.pop('delivery_address')
        
        
        for item in order:
            item['ordered_by'] =  self.get_ordered_by()
            order_serializer  =  ProductOrderSerializer(data=item)
            order_serializer.is_valid(raise_exception= True)
            order_instance  =  order_serializer.save()
            delivery_address['order_id'] =  order_instance.id
            delivery_address_serialzer  =  DeliveryAdressSerializer(data=delivery_address)
            delivery_address_serialzer.is_valid(raise_exception=True)
            delivery_address_serialzer.save()
            CartModel.objects.filter(id= item.get('cart_id')).update(status  =  False)
            
        return order_instance


class OrdersStatusSerializer(ModelSerializer):


    class Mets:
        model  =  OrdersStatusModel
        feilds  =  ["id," "order_id", "order_status", "order_remarks", "created_by", "created_on"]
        read_only_feilds = ['id', 'created_on']