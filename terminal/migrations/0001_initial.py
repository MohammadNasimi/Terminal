# Generated by Django 4.1.2 on 2022-10-06 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codebus', models.CharField(max_length=20)),
                ('usebus', models.CharField(max_length=20)),
                ('productionyear', models.CharField(max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.driver')),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hourmove', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('busRoute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.busroute')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('numberstation', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
                ('timeroute', models.PositiveIntegerField()),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.manager')),
            ],
        ),
        migrations.AddField(
            model_name='busroute',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.route'),
        ),
    ]