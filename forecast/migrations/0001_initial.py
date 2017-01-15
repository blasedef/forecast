# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20170114141224 on 2017-01-15 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_starts', models.DateTimeField(verbose_name='start date of rate')),
                ('date_ends', models.DateTimeField(verbose_name='end date of rate')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField(verbose_name='date of entry')),
                ('interval_date', models.DateTimeField(verbose_name='interval')),
                ('previous_amount', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
                ('income', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
                ('expense', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
                ('net', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
                ('next_amount', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
                ('manual_entry', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(verbose_name='date of transaction')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=23)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.TransactionMethod'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payee', to='forecast.Thirdparty'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='forecast.Thirdparty'),
        ),
        migrations.AddField(
            model_name='statement',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.Thirdparty'),
        ),
        migrations.AddField(
            model_name='statement',
            name='next_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next', to='forecast.Statement'),
        ),
        migrations.AddField(
            model_name='statement',
            name='previous_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prev', to='forecast.Statement'),
        ),
        migrations.AddField(
            model_name='rate',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.Thirdparty'),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.Thirdparty'),
        ),
    ]