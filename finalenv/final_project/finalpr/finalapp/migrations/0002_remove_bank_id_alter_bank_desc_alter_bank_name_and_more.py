# Generated by Django 4.2.2 on 2023-11-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='id',
        ),
        migrations.AlterField(
            model_name='bank',
            name='desc',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='bank',
            table='bankdb',
        ),
    ]
