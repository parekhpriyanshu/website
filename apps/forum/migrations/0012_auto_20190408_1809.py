# Generated by Django 2.0.8 on 2019-04-08 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20190408_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent_comment',
            old_name='to_uids',
            new_name='to_Parent_Comments',
        ),
    ]
