# Generated by Django 4.1.4 on 2023-03-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_payments_cost_of_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='cost_of_treatment',
            field=models.IntegerField(null=True),
        ),
    ]
