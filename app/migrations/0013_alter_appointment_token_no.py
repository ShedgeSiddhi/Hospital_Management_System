# Generated by Django 4.1.4 on 2023-03-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_doctor_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='token_no',
            field=models.IntegerField(null=True),
        ),
    ]
