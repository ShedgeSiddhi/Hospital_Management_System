# Generated by Django 4.1.4 on 2023-03-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_patient_payment_invoice_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_payment',
            name='invoice_date',
            field=models.CharField(max_length=100),
        ),
    ]
