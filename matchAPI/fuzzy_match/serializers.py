from rest_framework import serializers
from fuzzy_match.models import Shopify_db,Tasteguru_db,SP_TS_Bridge

class Shopify_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopify_db
        fields = 'SP_item_name'

class Tasteguru_dbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasteguru_db
        fields = 'TG_item_name'

class SP_TS_Bridge_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SP_TS_Bridge
        fields = '__all__'