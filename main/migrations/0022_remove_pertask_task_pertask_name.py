# Generated by Django 4.1.4 on 2023-02-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_pertask_date_alter_pertask_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pertask',
            name='task',
        ),
        migrations.AddField(
            model_name='pertask',
            name='name',
            field=models.CharField(default='kkk', max_length=50),
            preserve_default=False,
        ),
    ]
