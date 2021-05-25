# Generated by Django 3.2.3 on 2021-05-24 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bug_ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugticket',
            name='assigned_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugticket',
            name='completed_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_completed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugticket',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')], default='New', max_length=15),
        ),
    ]
