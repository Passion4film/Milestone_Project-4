# Generated by Django 3.2.6 on 2022-01-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=models.TextField(),
        ),
    ]
