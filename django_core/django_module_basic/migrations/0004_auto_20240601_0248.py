# Generated by Django 3.2 on 2024-06-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_module_basic', '0003_modeltest_class_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltest',
            name='arrival_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modeltest',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]