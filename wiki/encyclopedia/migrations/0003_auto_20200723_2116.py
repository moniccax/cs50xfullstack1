# Generated by Django 3.0.8 on 2020-07-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0002_auto_20200723_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.CharField(max_length=300, null=True),
        ),
    ]