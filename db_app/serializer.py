from rest_framework import serializers
from . views import Albums, Artists, Tracks


class SerializersAllalbum(serializers.ModelSerializer):

    class Meta:
        model = Albums
        fields = "__all__"


class SerializersArtists(serializers.ModelSerializer):

    class Meta:
        model = Artists
        fields = "__all__"


class SerializersTracks(serializers.ModelSerializer):

    class Meta:
        model = Tracks
        fields = "__all__"
