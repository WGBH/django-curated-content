# Generated by Django 2.1.7 on 2019-02-13 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curcon', '0002_curatedcontentinstance_instance_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curatedcontentinstance',
            name='content_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curcon.CuratedContentBlock'),
        ),
    ]
