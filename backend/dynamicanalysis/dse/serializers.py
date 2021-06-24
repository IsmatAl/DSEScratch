from rest_framework import serializers


class PexSerializer(serializers.Serializer):
    generated_inputs = serializers.ListField()
    output = serializers.ListField(
        child=serializers.IntegerField()
    )


class OptionsSerializer(serializers.Serializer):
    id = serializers.CharField()
    max_iters = serializers.IntegerField()
    pse = serializers.BooleanField()


class ProgramPairingSerializer(serializers.Serializer):
    id = serializers.CharField()


class RandomSampling(serializers.Serializer):
    low = serializers.IntegerField(default=-1000)
    high = serializers.IntegerField(default=1000)
    size = serializers.IntegerField(default=100)
    # solution = serializers.CharField()
    # submission = serializers.CharField()
    entry = serializers.CharField()
    # varSize = serializers.IntegerField()


class IdBody(serializers.Serializer):
    id = serializers.CharField()
