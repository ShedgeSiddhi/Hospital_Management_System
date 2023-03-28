# Generated by Django 4.1.4 on 2023-03-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_patient_address_alter_patient_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default=1, max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]
