# Generated by Django 3.2.16 on 2022-11-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='fee',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Называние тарифа'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fee',
            field=models.FloatField(),
        ),
    ]
