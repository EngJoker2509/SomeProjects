# Generated by Django 3.0 on 2022-12-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=5, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('age', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
