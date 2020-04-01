from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('documents', '0027_auto_20150824_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVersionBlock',
            fields=[
                (
                    'id', models.AutoField(
                        verbose_name='ID', serialize=False, auto_created=True,
                        primary_key=True
                    )
                ),
                (
                    'document', models.ForeignKey(
                        on_delete=models.CASCADE, to='documents.Document',
                        verbose_name='Document'
                    )
                ),
            ],
            options={
                'verbose_name': 'New version block',
                'verbose_name_plural': 'New version blocks',
            },
            bases=(models.Model,),
        ),
    ]
