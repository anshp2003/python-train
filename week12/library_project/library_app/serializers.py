from rest_framework import serializers
from .models import Author, genres, Book, BorrowedRecord
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

# Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genres
        fields = ['id', 'name']

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested relationship
    genres = GenreSerializer(many=True)  # Many-to-many relationship

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'publication_date', 'author', 'genres', 'is_available']

    def create(self, validated_data):
        # Extract nested data for author and genres
        author_data = validated_data.pop('author')
        genres_data = validated_data.pop('genres')

        # Check if the book already exists
        book_exists = Book.objects.filter(
            title=validated_data['title'],
            publication_date=validated_data['publication_date']
        ).first()

        if book_exists:
            # Check if the author name matches
            if book_exists.author.name == author_data.get('name'):
                raise serializers.ValidationError("This book already exists by this author.")

        # Create or get the author
        author, created = Author.objects.get_or_create(**author_data)

        # Create the book instance with the author
        book = Book.objects.create(author=author, **validated_data)

        # Create or get the genres and associate them with the book
        for genre_data in genres_data:
            genre, created = genres.objects.get_or_create(**genre_data)
            book.genres.add(genre)

        return book
    
# BorrowRecord Serializer
class BorrowRecordSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowedRecord
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date', 'status']
