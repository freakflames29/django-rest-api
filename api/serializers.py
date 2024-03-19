from rest_framework import serializers

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
        
    def update(self,instance,validate_data):
        instance.name=validate_data.get("name",instance.name)
        instance.price=validate_data.get("price",instance.price)
        instance.category=validate_data.get("category",instance.category)
        instance.save()
        return instance