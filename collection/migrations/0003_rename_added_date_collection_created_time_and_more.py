# Generated by Django 4.1 on 2023-04-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='added_date',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='user',
            new_name='custom_user',
        ),
        migrations.RenameField(
            model_name='game_blacklist',
            old_name='user',
            new_name='custom_user',
        ),
        migrations.RenameField(
            model_name='game_wishlist',
            old_name='user',
            new_name='custom_user',
        ),
        migrations.AddField(
            model_name='collection',
            name='delete_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
