# Generated by Django 3.2.20 on 2023-08-21 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0020_cliente_id_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_endereco',
            field=models.JSONField(blank=True, default=list),
        ),
    ]