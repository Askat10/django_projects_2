from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    quantity = serializers.IntegerField()