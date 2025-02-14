# Generated by Django 5.0.10 on 2025-01-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_status_queue_queue_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('record_status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended'), ('deleted', 'Deleted')], default='active', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='record_status',
            field=models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='record_status',
            field=models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='queue',
            name='record_status',
            field=models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='equipment',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='api.attribute'),
        ),
    ]
