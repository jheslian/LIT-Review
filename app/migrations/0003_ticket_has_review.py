# Generated by Django 4.0.3 on 2022-04-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_review_body_alter_review_headline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='has_review',
            field=models.BooleanField(default=False),
        ),
    ]