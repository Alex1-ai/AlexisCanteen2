# Generated by Django 3.2.13 on 2023-01-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(),
        ),
    ]
