# Generated by Django 4.2.10 on 2024-02-29 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendeer', '0002_rename_events_to_attendees_eventsattendees'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsInvitees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='eventName',
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='EventsAttendees',
        ),
        migrations.AddField(
            model_name='eventsinvitees',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='calendeer.event'),
        ),
        migrations.AddField(
            model_name='eventsinvitees',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
