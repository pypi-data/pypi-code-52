# Generated by Django 2.2.6 on 2019-10-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("katka", "0019_scmsteprun_sequence_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="scmrelease", name="scm_pipeline_run",),
        migrations.AddField(
            model_name="scmrelease", name="scm_pipeline_runs", field=models.ManyToManyField(to="katka.SCMPipelineRun"),
        ),
        migrations.AddField(
            model_name="scmrelease",
            name="status",
            field=models.CharField(choices=[("open", "open"), ("closed", "closed")], default="open", max_length=30),
        ),
    ]
