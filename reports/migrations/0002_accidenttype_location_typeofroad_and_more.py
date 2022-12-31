# Generated by Django 4.1.2 on 2022-12-21 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfRoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='witness_involvement',
            field=models.BooleanField(default=1, verbose_name='Were you involved?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='accident_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.accidenttype'),
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.location'),
        ),
        migrations.AlterField(
            model_name='report',
            name='type_of_road',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.typeofroad'),
        ),
    ]