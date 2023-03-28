# Generated by Django 4.1.4 on 2023-03-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_payment_admission_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('patient_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('admission_date', models.CharField(max_length=100)),
                ('discharge_date', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('advance_paid', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('card_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
