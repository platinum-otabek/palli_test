from rest_framework import serializers

from trade.models.Detail import DetailModel


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailModel
        fields = '__all__'
