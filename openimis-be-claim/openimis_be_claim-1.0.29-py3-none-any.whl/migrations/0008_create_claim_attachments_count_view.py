# Generated by Django 2.1.14 on 2020-03-30 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0007_auto_20200318_1443'),
    ]

    operations = [
        migrations.RunSQL(
            'CREATE VIEW claim_ClaimAttachmentsCountView AS select claim_id, count(*) attachments_count from claim_ClaimAttachment GROUP BY claim_id'
        ),
    ]
