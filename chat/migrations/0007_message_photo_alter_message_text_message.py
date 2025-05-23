# Generated by Django 5.1.4 on 2025-04-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_creted_chattwouser_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='saved_message_photos/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text_message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
