# Generated by Django 4.0.4 on 2024-03-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
