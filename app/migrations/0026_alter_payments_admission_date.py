# Generated by Django 4.1.4 on 2023-03-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_service_description_payments_cost_of_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='admission_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
