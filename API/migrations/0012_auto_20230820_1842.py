# Generated by Django 3.2.20 on 2023-08-20 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_auto_20230820_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='API.cliente'),
        ),
        migrations.AlterField(
            model_name='clienteendereco',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes_associados', to='API.endereco'),
        ),
    ]
