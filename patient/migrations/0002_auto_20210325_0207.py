# Generated by Django 3.1.5 on 2021-03-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_fname',
            field=models.CharField(max_length=255, verbose_name='First Name Hindi'),
        ),
    ]
