# Generated by Django 4.0.4 on 2022-04-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0002_client_alter_project_date_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
