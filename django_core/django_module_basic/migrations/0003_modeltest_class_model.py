# Generated by Django 3.2 on 2024-05-31 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_module_basic', '0002_area_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltest',
            name='class_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modeltests', to='django_module_basic.class'),
            preserve_default=False,
        ),
    ]
