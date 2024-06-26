# Generated by Django 5.0.6 on 2024-06-23 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subb_category', to='product_module.category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_category', to='product_module.category'),
        ),
    ]
