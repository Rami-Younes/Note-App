# Generated by Django 3.0.6 on 2020-06-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default='', upload_to='notes-img'),
            preserve_default=False,
        ),
    ]
