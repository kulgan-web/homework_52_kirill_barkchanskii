# Generated by Django 4.2.7 on 2023-11-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, verbose_name='Описание задачи')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Статус задачи')),
                ('date_of_completion', models.TextField(null=True, verbose_name='Дата выполнения YYYY-mm-dd')),
            ],
        ),
    ]