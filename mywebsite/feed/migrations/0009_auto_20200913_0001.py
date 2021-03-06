# Generated by Django 3.1.1 on 2020-09-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_search'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.RenameField(
            model_name='search',
            old_name='terms',
            new_name='term',
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['term'], name='feed_search_term_d64608_idx'),
        ),
    ]
