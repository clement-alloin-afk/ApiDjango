# Generated by Django 4.0.1 on 2022-06-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_produit_mesure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='quantityAutoAdd',
            field=models.IntegerField(null=True),
        ),
    ]