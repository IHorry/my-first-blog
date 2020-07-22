# Generated by Django 2.2.12 on 2020-07-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200713_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='dateEnd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='dateStarted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
