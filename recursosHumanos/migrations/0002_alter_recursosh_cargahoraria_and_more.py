# Generated by Django 4.2.2 on 2023-06-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursosHumanos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursosh',
            name='cargaHoraria',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='recursosh',
            name='folhaPonto',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='recursosh',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
