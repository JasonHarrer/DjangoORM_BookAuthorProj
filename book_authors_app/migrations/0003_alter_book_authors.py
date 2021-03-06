# Generated by Django 3.2.6 on 2021-08-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='book_authors_app.Author'),
        ),
    ]
