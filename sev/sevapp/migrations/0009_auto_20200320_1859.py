# Generated by Django 3.0.3 on 2020-03-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevapp', '0008_auto_20200320_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='election',
            name='start_date',
            field=models.DateField(),
        ),
    ]