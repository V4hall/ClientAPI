# Generated by Django 3.2.20 on 2023-08-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20230820_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='API.cliente'),
        ),
    ]
