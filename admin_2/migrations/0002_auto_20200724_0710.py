# Generated by Django 3.0.7 on 2020-07-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donorinfo',
            name='disease',
        ),
        migrations.AddField(
            model_name='donorinfo',
            name='disease',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Disease',
        ),
    ]
