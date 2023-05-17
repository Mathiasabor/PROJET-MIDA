# Generated by Django 4.2.1 on 2023-05-04 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('nom', models.CharField(max_length=255)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Telecharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField()),
                ('thesed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.theses')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('linodate', models.CharField(max_length=100)),
                ('editions', models.CharField(max_length=255)),
                ('exemplaire', models.IntegerField()),
                ('categoried', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Consultes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('livred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.livre')),
            ],
        ),
    ]
