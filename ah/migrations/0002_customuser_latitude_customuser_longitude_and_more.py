# Generated by Django 4.1.4 on 2022-12-22 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='latitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='longitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='case',
            name='worker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='worker_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
