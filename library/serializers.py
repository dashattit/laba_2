from rest_framework import serializers
from .models import Book, Author

#класс наследуется от serializers.ModelSerializer, т.е мы автоматически создаем сериализатор на основе модели book
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  #используем строковое представление автора

    class Meta:
        model = Book
        #список полей, которые будут включены  сериализацию
        fields = ['title', 'year_of_publication', 'publisher', 'book_type', 'author']

    #валидация входных данных перед их сохранением
    def validate(self, attrs):
        #проверка на уникальность автора
        author_data = attrs.get('author')
        author_name = author_data.get('name')

        if Author.objects.filter(name=author_name).exists():
            raise serializers.ValidationError({"author": "Автор с таким именем уже существует."})

        # Проверка на уникальность книги
        book_type = attrs.get('book_type')
        existing_book = Book.objects.filter(
            title=attrs['title'],
            author__name=author_name,
            year_of_publication=attrs['year_of_publication'],
            publisher=attrs['publisher'],
            book_type=book_type
        ).exists()

        if existing_book:
            raise serializers.ValidationError(
                "Книга с таким названием, автором, годом издания и издательством уже существует.")
        return attrs

    #создание экземпляра книги
    def create(self, validated_data):
        #извлекаем данные автора из проверенных данных
        #pop-удаляет поле author, чтобы его не передавать в создание экземпляра книги
        author_data = validated_data.pop('author')
        #создаем или получаем экземпляр автора
        author, created = Author.objects.get_or_create(**author_data)

        book_type = validated_data.get('book_type')

        if book_type == 'textbook':
            #проверка на уникальность для учебников
            existing_book = Book.objects.filter(
                title=validated_data['title'],
                author=author,
                year_of_publication=validated_data['year_of_publication'],
                publisher=validated_data['publisher'],
                book_type='textbook'
            ).first()

            if existing_book:
                raise serializers.ValidationError("Учебник с таким издателем и годом издания уже существует.")

        #создаем экземпляр книги с автором
        book = Book.objects.create(author=author, **validated_data)
        return book

#сериализатор для автора
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  #вложенный сериализатор для книг

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']  #включаем необходимые поля