# Generated by Django 2.0.8 on 2019-03-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_headlines_conent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headlines',
            options={'ordering': ('-add_time',)},
        ),
    ]