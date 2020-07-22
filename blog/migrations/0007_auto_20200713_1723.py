# Generated by Django 2.2.12 on 2020-07-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200708_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.TextField()),
                ('dateStarted', models.DateTimeField(blank=True, null=True)),
                ('dateEnd', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cv',
            name='WorkExp',
        ),
    ]
