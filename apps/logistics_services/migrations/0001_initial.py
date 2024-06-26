# Generated by Django 5.0.4 on 2024-04-22 09:48

import apps.logistics_services.models.services
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticsService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Logistics Service',
                'verbose_name_plural': 'Logistics Services',
                'db_table': 'logistics_services',
                'ordering': ['id', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='LogisticsServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Logistics Service Type',
                'verbose_name_plural': 'Logistics Service Types',
                'db_table': 'logistics_service_types',
                'ordering': ['id', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='LogisticsServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to=apps.logistics_services.models.services.logistics_image_upload_location, verbose_name='Image')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='logistics_services.logisticsservice')),
            ],
            options={
                'verbose_name': 'Logistics Service Image',
                'verbose_name_plural': 'Logistics Service Images',
                'db_table': 'logistics_service_images',
                'ordering': ['id', 'created_at'],
            },
        ),
        migrations.AddField(
            model_name='logisticsservice',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='logistics_services.logisticsservicetype'),
        ),
    ]
