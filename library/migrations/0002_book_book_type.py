# Generated by Django 5.1.4 on 2024-12-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('fiction', 'Художественное произведение'), ('textbook', 'Учебник')], max_length=10, null=True),
        ),
    ]
