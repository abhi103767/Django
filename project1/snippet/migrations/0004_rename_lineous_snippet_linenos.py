# Generated by Django 4.1.4 on 2023-01-24 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0003_snippet_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineous',
            new_name='linenos',
        ),
    ]
