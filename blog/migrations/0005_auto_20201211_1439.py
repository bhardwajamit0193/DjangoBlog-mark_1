# Generated by Django 3.1.3 on 2020-12-11 09:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_body_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_text',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
