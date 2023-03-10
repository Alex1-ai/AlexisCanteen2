# Generated by Django 3.2.13 on 2023-01-06 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('service_image', models.ImageField(blank=True, upload_to='services/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shops/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.shop')),
            ],
        ),
    ]
