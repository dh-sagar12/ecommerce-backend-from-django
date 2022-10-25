from rest_framework.serializers import ModelSerializer

from stocks.models.StockModels import StockModel


class ProductItemStockSerializer(ModelSerializer):

    class Meta:
        model = StockModel
        fields  = ['id', 'product_id', 'product_inventory_id', 'stock_qty', 'statement_reference']
        read_only_fields = ['id', 'created_on', 'updated_on']