from rest_framework import serializers

from nestedCrud.models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']
        read_only_fields = ['singer']
"""NEST$ED CRUD SINGER THROUNG SONGSERIALIZER"""
        # def create(self, validated_data):
        #     singer = validated_data.pop('singer')
        #     singer= Singer.objects.create(**singer)
        #     song = Song.objects.create(**validated_data, singer=singer)
        #     return song

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # song_set = SongSerializer(many=True)
    # song =serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song = SongSerializer(many=True)
    # depth = 1
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    # song = serializers.StringRelatedField(many=True)
    # songUrl = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','age','song']
        # read_only_fields = ['song']

    def create(self, validated_data):
        song_data = validated_data.pop('song')
        singer = Singer.objects.create(**validated_data)
        for song in song_data:
            Song.objects.create(singer=singer, **song)
        return singer