# Generated by Django 4.2.10 on 2024-03-01 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendeer', '0004_remove_eventsinvitees_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsinvitees',
            name='event',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.DO_NOTHING, to='calendeer.event'),
            preserve_default=False,
        ),
    ]