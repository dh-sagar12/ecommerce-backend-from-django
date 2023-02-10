from rest_framework import serializers

from account.models.user import  ShippingDetailMOdel

class ShippingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingDetailMOdel
        fields =  ['id', 'full_name', 'user_id', 'address', 'postal_code', 'city', 'landmark', 'contact_number' ]    
        read_only_fields = ['id']

    
    def get_user_id(self, obj):
        print('user',self.context['request'].user )
        return self.context['request'].user