# Generated by Django 5.0.6 on 2024-06-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_otpcode_code_alter_otpcode_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
