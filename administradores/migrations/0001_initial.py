# Generated by Django 4.2.11 on 2024-03-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('administrador', models.CharField(max_length=45)),
                ('nombreAdministrador', models.CharField(max_length=30)),
                ('contrasenia', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Adimistradores',
            },
        ),
    ]
