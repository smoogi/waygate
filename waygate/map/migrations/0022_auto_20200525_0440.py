# Generated by Django 3.0.6 on 2020-05-25 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0021_auto_20200525_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narrator',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='map.Character'),
        ),
    ]