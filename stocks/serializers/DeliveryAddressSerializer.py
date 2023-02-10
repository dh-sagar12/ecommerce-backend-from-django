from rest_framework import serializers

from stocks.models.OrderModels import DeliveryAdressModel


class DeliveryAdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAdressModel
        fields =  ['id', 'full_name', 'order_id', 'address', 'postal_code', 'city', 'landmark', 'contact_number' ]    
        read_only_fields = ['id']