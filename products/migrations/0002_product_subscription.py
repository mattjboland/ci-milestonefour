# Generated by Django 3.1.3 on 2020-11-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subscription',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]