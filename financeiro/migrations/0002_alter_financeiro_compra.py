# Generated by Django 4.2.2 on 2023-06-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeiro',
            name='compra',
            field=models.CharField(max_length=50),
        ),
    ]
