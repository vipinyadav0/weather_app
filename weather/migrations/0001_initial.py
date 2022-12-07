# Generated by Django 4.1.1 on 2022-12-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Las Vegas', max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
            },
        ),
    ]