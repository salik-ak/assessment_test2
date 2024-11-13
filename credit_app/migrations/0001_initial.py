# Generated by Django 5.1.3 on 2024-11-13 10:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('option_a', models.CharField(max_length=50)),
                ('option_b', models.CharField(max_length=50)),
                ('option_c', models.CharField(max_length=50)),
                ('option_d', models.CharField(max_length=50)),
                ('score_a', models.IntegerField(default=0)),
                ('score_b', models.IntegerField(default=0)),
                ('score_c', models.IntegerField(default=0)),
                ('score_d', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_option', models.CharField(max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit_app.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]