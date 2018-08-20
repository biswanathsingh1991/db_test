from rest_framework import serializers
from . views import Albums


class SerializersAllalbum(serializers.ModelSerializer):

    class Meta:
        model = Albums
        fields = "__all__"
