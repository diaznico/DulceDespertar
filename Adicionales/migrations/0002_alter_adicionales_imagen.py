# Generated by Django 3.2.9 on 2021-11-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adicionales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adicionales',
            name='imagen',
            field=models.ImageField(upload_to='adicionales'),
        ),
    ]
