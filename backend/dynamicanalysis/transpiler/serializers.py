from rest_framework import serializers


class PythonConversionSerializer(serializers.Serializer):
    fileNames = serializers.ListField(
        child=serializers.CharField()
    )


class FileUploadSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField()
    )
    entry = serializers.CharField()
