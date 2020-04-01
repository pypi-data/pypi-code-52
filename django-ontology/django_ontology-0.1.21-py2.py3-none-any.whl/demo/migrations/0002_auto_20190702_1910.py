# Generated by Django 2.2.3 on 2019-07-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='static_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='used_in_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='concept',
            name='static_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='concept',
            name='used_in_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='definition',
            name='static_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='definition',
            name='used_in_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='concept',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='concept',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='concept',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='definition',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='definition',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='definition',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
