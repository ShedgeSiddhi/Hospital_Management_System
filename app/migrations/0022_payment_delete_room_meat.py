# Generated by Django 4.1.4 on 2023-03-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_room_meat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('patient_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('admission_date', models.CharField(max_length=100)),
                ('discharge_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Room_meat',
        ),
    ]