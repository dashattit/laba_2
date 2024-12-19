from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        label='Автор',
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'year_of_publication',
                  'genre', 'category', 'publisher', 'cover_image',
                  'text_file', 'url']

    def validate(self, attrs):
        author_id = attrs.get('author_id')
        if author_id:
            try:
                author = Author.objects.get(id=author_id)  # извлекаем экземпляр author
                attrs['author'] = author  # добавляем в attrs для использования
            except Author.DoesNotExist:
                raise serializers.ValidationError({"author": "Автор не найден."})
        return attrs

    def create(self, validated_data):
        author = validated_data.pop('author')
        book = Book.objects.create(author=author, **validated_data)
        return book

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # вложенный сериализатор для книг

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']  # указываем необходимые поля