# Generated by Django 4.0.4 on 2022-05-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0004_pageexemple'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageexemple',
            name='date',
            field=models.DateField(default='2022-05-23', verbose_name='Date de mise en place du site'),
        ),
    ]