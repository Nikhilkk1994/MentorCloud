# Generated by Django 3.1.5 on 2021-01-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of Package')),
                ('description', models.TextField(max_length=5000, verbose_name='Description of Package')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='media/package/')),
            ],
            options={
                'verbose_name': 'Package Session',
                'verbose_name_plural': 'Package Sessions',
            },
        ),
    ]
