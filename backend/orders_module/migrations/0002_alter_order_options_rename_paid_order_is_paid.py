# Generated by Django 5.0.6 on 2024-06-28 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('is_paid', '-created_date', '-updated_date')},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='is_paid',
        ),
    ]