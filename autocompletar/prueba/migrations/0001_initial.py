# Generated by Django 2.1.3 on 2018-11-14 16:22

from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug_Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_inicio', month.models.MonthField()),
            ],
        ),
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prueba.Concepto')),
            ],
        ),
        migrations.AddField(
            model_name='bug_movimiento',
            name='concepto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prueba.Concepto'),
        ),
    ]
