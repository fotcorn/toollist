# Generated by Django 2.0.7 on 2018-07-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toollist', '0003_toolentry_apm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolentry',
            name='number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Number'),
        ),
        migrations.AlterUniqueTogether(
            name='toolentry',
            unique_together=set(),
        ),
    ]
