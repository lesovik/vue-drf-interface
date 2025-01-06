# Generated by Django 5.0.10 on 2024-12-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_queue_name_alter_queue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('completed', 'Completed'), ('processing', 'Processing')], max_length=500),
        ),
    ]
