# Generated by Django 4.2.2 on 2023-06-08 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at_alter_todo_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'To Do', 'verbose_name_plural': 'To Do List'},
        ),
    ]