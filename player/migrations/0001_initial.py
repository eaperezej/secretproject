# Generated by Django 4.0.4 on 2022-05-20 03:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('goals', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Goals')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='team.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
