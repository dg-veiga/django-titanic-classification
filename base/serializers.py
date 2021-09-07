from .models import TitanicTrain, TitanicTest

from rest_framework import serializers

# ======= New Serializers =======
class TitanicTrainSerialized(serializers.ModelSerializer):
    class Meta:
        model = TitanicTrain      
        fields = '__all__'