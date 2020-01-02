# Generated by Django 3.0.1 on 2020-01-02 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scode', models.CharField(max_length=50, unique=True)),
                ('sname', models.CharField(max_length=50)),
                ('sprice', models.CharField(max_length=50)),
                ('stype', models.CharField(max_length=50)),
                ('screated', models.DateTimeField(auto_now_add=True)),
                ('screated_by', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'Service',
            },
        ),
    ]
