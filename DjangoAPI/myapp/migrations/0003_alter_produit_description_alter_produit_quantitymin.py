# Generated by Django 4.0.1 on 2022-02-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='quantityMin',
            field=models.IntegerField(null=True),
        ),
    ]