# Generated by Django 3.1.1 on 2020-09-07 10:11

from django.db import migrations, models
import tags.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20200907_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='video',
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=30, unique=True, validators=[tags.validators.title]),
        ),
    ]
