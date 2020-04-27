# Generated by Django 3.0.4 on 2020-04-21 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materiel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'matériel',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(max_length=200, unique=True)),
                ('login', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'inventaire',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, unique=True)),
                ('materiel', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.Materiel')),
            ],
            options={
                'verbose_name': 'propriétaire',
            },
        ),
    ]