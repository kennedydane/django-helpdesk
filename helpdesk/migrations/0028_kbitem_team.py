# Generated by Django 2.2.9 on 2020-01-27 15:01

from django.db import migrations, models
import django.db.models.deletion

from helpdesk import settings as helpdesk_settings


class Migration(migrations.Migration):
    dependencies = [
        ("helpdesk", "0027_auto_20200107_1221"),
    ] + helpdesk_settings.HELPDESK_TEAMS_MIGRATION_DEPENDENCIES

    operations = [
        migrations.AddField(
            model_name="kbitem",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=helpdesk_settings.HELPDESK_TEAMS_MODEL,
                verbose_name="Team",
            ),
        ),
    ]
