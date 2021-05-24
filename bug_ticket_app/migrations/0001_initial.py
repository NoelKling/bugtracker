# Generated by Django 3.2.3 on 2021-05-24 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')], max_length=15)),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_assigned', to=settings.AUTH_USER_MODEL)),
                ('completed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_completed', to=settings.AUTH_USER_MODEL)),
                ('filed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_problem', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
