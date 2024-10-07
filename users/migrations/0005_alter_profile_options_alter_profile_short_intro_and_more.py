# Generated by Django 5.0.6 on 2024-07-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, default='This is a default bio. User has not added a bio yet.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='Earth', max_length=200, null=True),
        ),
    ]
