# Generated by Django 3.2.9 on 2021-12-06 06:57

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


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
                ('description', models.CharField(max_length=300)),
                ('liked_by', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), null=True, size=None)),
                ('liked_by_count', models.IntegerField(default=0, null=True)),
                ('path', models.CharField(default='/', max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='postauthor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('liked_by', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), null=True, size=None)),
                ('liked_by_count', models.IntegerField(default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.post')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentauthor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
