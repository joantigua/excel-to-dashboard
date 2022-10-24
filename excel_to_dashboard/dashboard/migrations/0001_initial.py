# Generated by Django 4.1.2 on 2022-10-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('qa', models.FloatField(null=True)),
                ('ce', models.FloatField(null=True)),
                ('csat', models.FloatField(null=True)),
                ('aht', models.DurationField(null=True)),
                ('hc', models.FloatField(null=True)),
            ],
        ),
    ]
