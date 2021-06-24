from rest_framework import serializers


class CodeCoverageSerializer(serializers.Serializer):
    entry = serializers.CharField()
    # id = serializers.CharField()
    # inputs = serializers.ListField()
    # expectedOutputs = serializers.ListField(required=False)
