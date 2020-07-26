# Generated by Django 3.0.7 on 2020-07-26 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_2', '0003_auto_20200724_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='disease',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='motivateddonortable',
            name='donor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_2.donorInfo'),
        ),
    ]
