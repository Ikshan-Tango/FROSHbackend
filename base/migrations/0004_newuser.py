# Generated by Django 4.0.6 on 2022-07-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_branch_branches'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_number', models.CharField(max_length=6)),
                ('pwd', models.CharField(max_length=8)),
            ],
        ),
    ]
