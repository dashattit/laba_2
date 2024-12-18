from django.db import models

#создаем модель автора
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

#создаем модель книги с необходимыми полями
class Book(models.Model):
    BOOK_TYPE_CHOICES = [
        ('fiction', 'Художественное произведение'),
        ('textbook', 'Учебник'),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year_of_publication = models.IntegerField()
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    text_file = models.FileField(upload_to='books/')
    book_type = models.CharField(max_length=10, choices=BOOK_TYPE_CHOICES, null=True)

    class Meta:
        unique_together = ('title', 'author', 'year_of_publication', 'publisher')

    def __str__(self):
        return self.title
