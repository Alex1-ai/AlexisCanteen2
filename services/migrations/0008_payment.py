# Generated by Django 3.2.3 on 2024-09-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_order_service_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField()),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
