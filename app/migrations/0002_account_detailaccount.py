# Generated by Django 5.0.6 on 2024-05-19 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetailAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('id_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='app.account')),
            ],
        ),
    ]
