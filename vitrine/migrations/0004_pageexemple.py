# Generated by Django 4.0.4 on 2022-05-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0003_alter_client_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageExemple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='sites/')),
                ('page', models.CharField(max_length=50)),
            ],
        ),
    ]