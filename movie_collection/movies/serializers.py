from rest_framework import serializers
from .models import Collection, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Collection
        fields = ['uuid', 'title', 'description', 'movies', 'user']

    def create(self, validated_data):
        movies_data = validated_data.pop('movies', [])
        collection = Collection.objects.create(**validated_data)

        for movie_data in movies_data:
            movie, created = Movie.objects.update_or_create(
                uuid=movie_data['uuid'], defaults=movie_data
            )
            collection.movies.add(movie)

        return collection

    def update(self, instance, validated_data):
        movies_data = validated_data.pop('movies', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Clear existing movies and add updated movies
        instance.movies.clear()
        for movie_data in movies_data:
            movie, created = Movie.objects.update_or_create(
                uuid=movie_data['uuid'], defaults=movie_data
            )
            instance.movies.add(movie)

        return instance
