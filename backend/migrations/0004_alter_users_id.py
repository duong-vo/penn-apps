# Generated by Django 4.2.5 on 2023-09-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_articles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]