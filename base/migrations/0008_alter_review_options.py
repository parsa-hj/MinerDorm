# Generated by Django 4.1.3 on 2022-11-07 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_review_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
