# Generated by Django 3.2.3 on 2021-05-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_api', '0003_auto_20210525_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploads',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='knowledgedatabase',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
