# Generated by Django 2.1.5 on 2019-02-09 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='group',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='folder',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mails.Folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
