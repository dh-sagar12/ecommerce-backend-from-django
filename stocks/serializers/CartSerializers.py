from rest_framework.serializers import ModelSerializer
from stocks.models.CartModels import CartModel


class UserCartSerializer(ModelSerializer):
    
    class Meta:
        model = CartModel
        fields  = ['id', 'user_id',  'product_id', 'product_inventory_id', 'cart_qty', 'status',  'created_on']
        read_only_fields = ['id', 'created_on']
    
    def get_user_id(self, obj):
        return self.context['request'].user
    
    # def create(self, validated_data):
    #    user_id =  self.request.user
    #    cart_qty  =  validated_data.pop['cart_qty']
    #    product_inventory_id =  validated_data.pop['product_inventory_id']