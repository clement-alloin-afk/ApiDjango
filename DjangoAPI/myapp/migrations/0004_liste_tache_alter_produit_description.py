# Generated by Django 4.0.1 on 2022-02-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_produit_description_alter_produit_quantitymin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('isCheck', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
