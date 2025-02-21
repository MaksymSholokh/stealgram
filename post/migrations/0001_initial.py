# Generated by Django 5.1.4 on 2025-02-10 13:51

import django.db.models.deletion
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('rewrite_time', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(max_length=10000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=users.models.user_dir_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=users.models.user_dir_path)),
                ('status', models.CharField(choices=[('Pb', 'Published'), ('Dr', 'Draft')], default='Dr', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='post.post')),
            ],
        ),
    ]
