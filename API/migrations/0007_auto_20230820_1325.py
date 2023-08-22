# Generated by Django 3.2.20 on 2023-08-20 16:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20230820_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='enderecos',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]