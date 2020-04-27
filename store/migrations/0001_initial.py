# Generated by Django 3.0.4 on 2020-04-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(null=True, verbose_name='référence')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('available', models.BooleanField(default=True, verbose_name='disponible')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('picture', models.TextField(verbose_name="URL de l'image")),
            ],
            options={
                'verbose_name': 'disque',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'artiste',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'prospect',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="date d'envoi")),
                ('contacted', models.BooleanField(default=False, verbose_name='demande traitée ?')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Album')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Contact')),
            ],
            options={
                'verbose_name': 'réservation',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='albums', to='store.Artist'),
        ),
    ]