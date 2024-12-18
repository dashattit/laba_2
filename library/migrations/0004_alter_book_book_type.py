# Generated by Django 5.1.4 on 2024-12-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_biography_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('fiction', 'Художественное произведение'), ('textbook', 'Учебник')], max_length=10, null=True),
        ),
    ]